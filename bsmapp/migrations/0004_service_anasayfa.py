# Generated by Django 5.0.2 on 2025-06-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsmapp', '0003_about_desc2_alter_about_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='anasayfa',
            field=models.BooleanField(default=False),
        ),
    ]
