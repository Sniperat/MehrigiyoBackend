# Generated by Django 4.0.2 on 2022-07-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_usermodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/2022-7-7/'),
        ),
    ]
