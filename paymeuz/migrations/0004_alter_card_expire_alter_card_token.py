# Generated by Django 4.0.2 on 2022-03-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeuz', '0003_remove_card_type_alter_card_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expire',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='card',
            name='token',
            field=models.TextField(),
        ),
    ]
