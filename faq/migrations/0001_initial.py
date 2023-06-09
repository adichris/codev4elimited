# Generated by Django 4.2 on 2023-04-25 22:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(unique=True)),
                ('answer', tinymce.models.HTMLField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Frequently Asked Question',
                'verbose_name_plural': 'Frequently Asked Questions',
            },
        ),
    ]
