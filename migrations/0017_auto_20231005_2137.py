# Generated by Django 3.0 on 2023-10-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0016_guards_rlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guards',
            name='level',
            field=models.CharField(blank=True, default='  not get any training Level', max_length=100, null=True),
        ),
    ]
