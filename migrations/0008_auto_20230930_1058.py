# Generated by Django 3.0 on 2023-09-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0007_auto_20230930_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackinghistory',
            name='timeperiod',
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='fromdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='todate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
