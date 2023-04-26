import os
import random
import string
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


class UserProfileManager(UserManager):
    def create_user(self, first_name, last_name, email, phone_number=None, password=None):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number=None, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


def upload_picture(instance, filename):
    new_filename = instance.first_name.replace(" ", "")+str(instance.id)+os.path.splitext(filename)[-1]
    return os.path.join("profile", "pictures", new_filename)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=60, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=upload_picture)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name", )

    objects = UserProfileManager()

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return super(User, self).has_perm(perm, obj)

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        else:
            return super(User, self).has_module_perms(app_label)

    def has_perms(self, perm_list, obj=None):
        if self.is_superuser:
            return True
        return super(User, self).has_perms(perm_list, obj=obj)

    def get_short_name(self):
        return self.first_name

    def get_fullname(self):
        fname = self.first_name
        lname = self.last_name
        if fname.islower():
            fname = fname.title()
        if lname.islower():
            lname = lname.title()

        return fname + ' ' + lname

    def get_full_name(self):
        return self.get_fullname()


def user_slugify(sender, instance, **kwargs):
    if instance.email:
        user_slug = slugify(instance.email.split("@")[0])
    else:
        user_slug = slugify(instance.first_name, instance.last_name)
    try:
        User.objects.get(slug=user_slug)
    except User.DoesNotExist:
        # safe
        pass
    else:
        new_slug = list(string.digits + string.ascii_letters)
        random.shuffle(new_slug)
        random.shuffle(new_slug)
        user_slug = "".join(new_slug[:10])
    instance.slug = user_slug
    return instance


models.signals.pre_save.connect(user_slugify, sender=User)


class ContactUs(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=120, null=True, blank=True)
    company = models.CharField(max_length=120, null=True, blank=True)
    message = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us List'
