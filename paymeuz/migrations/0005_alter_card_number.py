# Generated by Django 4.0.2 on 2022-03-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeuz', '0004_alter_card_expire_alter_card_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
