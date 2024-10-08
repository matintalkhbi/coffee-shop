# Generated by Django 5.0.6 on 2024-08-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0013_alter_orderitem_price_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
    ]
