# Generated by Django 4.0.2 on 2022-07-07 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0005_advertising'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentdoctor',
            name='rate',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='commentmedicine',
            name='rate',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='commentdoctor',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comments_doc', to='specialist.doctor'),
        ),
    ]
