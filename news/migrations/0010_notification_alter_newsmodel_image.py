# Generated by Django 4.0.2 on 2022-11-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_advertising'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='notification/')),
                ('notification_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/2022-11-11/'),
        ),
    ]
