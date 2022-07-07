# Generated by Django 4.0.2 on 2022-07-07 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0017_alter_picturesmedicine_image'),
        ('comment', '0004_alter_commentdoctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdoctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentmedicine',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comments_med', to='shop.medicine'),
        ),
    ]
