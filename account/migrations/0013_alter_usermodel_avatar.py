# Generated by Django 4.0.2 on 2022-06-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/2022-6-6/'),
        ),
    ]
