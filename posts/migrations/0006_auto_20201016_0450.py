# Generated by Django 3.0 on 2020-10-16 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20201015_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='notification',
            new_name='notificated',
        ),
    ]
