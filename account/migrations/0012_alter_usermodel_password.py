# Generated by Django 4.0.2 on 2022-03-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
