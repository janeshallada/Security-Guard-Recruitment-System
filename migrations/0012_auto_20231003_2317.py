# Generated by Django 3.0 on 2023-10-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0011_auto_20231003_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guards',
            name='user1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
