# Generated by Django 4.0.2 on 2022-02-14 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='types/')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='review',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='type_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='specialist.typedoctor'),
        ),
    ]
