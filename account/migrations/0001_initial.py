# Generated by Django 4.0.2 on 2022-02-12 15:16

import config.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Пожалуйста, укажите свой пароль', max_length=15, unique=True, validators=[config.validators.PhoneValidator])),
                ('password', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()])),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/2022-2-2/')),
                ('language', models.CharField(blank=True, max_length=3, null=True)),
                ('theme_mode', models.SmallIntegerField(choices=[(2, 'Black'), (1, 'White')], db_index=True, default=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='CountyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmsAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=16)),
                ('counter', models.IntegerField(default=0)),
                ('last_attempt_at', models.DateTimeField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=16)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('code', models.CharField(max_length=10)),
                ('expire_at', models.DateTimeField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='account.countymodel')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('full_address', models.CharField(blank=True, max_length=255, null=True)),
                ('apartment_office', models.CharField(blank=True, max_length=255, null=True)),
                ('floor', models.CharField(blank=True, max_length=255, null=True)),
                ('door_or_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('instructions', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='account.regionmodel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='favorite_doctor',
            field=models.ManyToManyField(blank=True, to='specialist.Doctor'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='favorite_medicine',
            field=models.ManyToManyField(blank=True, to='shop.Medicine'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
