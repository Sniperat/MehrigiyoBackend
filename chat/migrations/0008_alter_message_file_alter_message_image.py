# Generated by Django 4.0.2 on 2022-10-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_chatroom_admin_alter_chatroom_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='message/files/2022-10-10/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='message/images/2022-10-10/'),
        ),
    ]
