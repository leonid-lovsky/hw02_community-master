# Generated by Django 2.2.19 on 2022-05-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220511_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
