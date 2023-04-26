# Generated by Django 4.2 on 2023-04-25 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us List'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 4, 25, 18, 30, 39, 473467, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]