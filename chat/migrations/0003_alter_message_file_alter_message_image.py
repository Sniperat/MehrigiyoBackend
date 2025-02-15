# Generated by Django 4.0.2 on 2022-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_msg_message_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='message/files/2022-3-3/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='message/images/2022-3-3/'),
        ),
    ]
