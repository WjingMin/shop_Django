# Generated by Django 3.0.4 on 2020-10-19 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201019_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wxuser',
            name='cateid',
        ),
    ]
