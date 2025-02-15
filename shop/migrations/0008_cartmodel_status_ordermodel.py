# Generated by Django 4.0.2 on 2022-03-06 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_alter_usermodel_avatar_card'),
        ('shop', '0007_cartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'active'), (2, 'done')], default=1),
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('payment_type', models.PositiveSmallIntegerField(choices=[(1, 'Оплата при доставке'), (2, 'Кредитная карта'), (3, 'Прямой банковский перевод')], default=2)),
                ('payment_status', models.PositiveSmallIntegerField(choices=[(1, 'В ожидании'), (2, 'Ошибка'), (3, 'Завершено'), (4, 'Отменен'), (5, 'Истёк'), (6, 'Возвращен')], default=1)),
                ('delivery_status', models.PositiveSmallIntegerField(choices=[(1, 'В ожидании'), (2, 'На доставке'), (3, 'Доставлен'), (4, 'Возвращен')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart_products', models.ManyToManyField(to='shop.CartModel')),
                ('credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.card')),
                ('shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.deliveryaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
