# Generated by Django 4.0.2 on 2022-03-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionmodel',
            name='delivery_price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
