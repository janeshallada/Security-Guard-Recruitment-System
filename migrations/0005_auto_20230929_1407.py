# Generated by Django 3.0 on 2023-09-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0004_auto_20230929_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guards',
            name='passphoto',
            field=models.FileField(blank=True, max_length=300, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='guards',
            name='pic',
            field=models.FileField(blank=True, max_length=300, null=True, upload_to='media/'),
        ),
    ]
