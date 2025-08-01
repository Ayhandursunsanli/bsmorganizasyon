# Generated by Django 5.0.2 on 2025-06-05 12:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Uzmanlarimiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='uzmanlar/')),
                ('job', models.CharField(max_length=255)),
            ],
        ),
    ]
