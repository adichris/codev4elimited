from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'picture', 'email', 'password', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    readonly_fields = ('date_joined', )

    list_display = ('__str__', 'email', 'last_login')
    list_filter = ('is_admin',)
    fieldsets = (
        ("Credential", {'fields': ('phone_number', 'password')}),
        ('Personal info', {'classes': ('wide',), 'fields': ('email', 'first_name', 'last_name', 'picture')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
        ('Status', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
