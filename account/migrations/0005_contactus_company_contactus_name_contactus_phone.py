# Generated by Django 4.2 on 2023-04-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_contactus_options_contactus_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
