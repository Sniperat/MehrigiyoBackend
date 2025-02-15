# Generated by Django 4.0.2 on 2022-02-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0002_typedoctor_doctor_created_at_doctor_description_and_more'),
        ('account', '0004_alter_usermodel_favorite_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='specialist_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='worker', to='specialist.doctor'),
        ),
    ]
