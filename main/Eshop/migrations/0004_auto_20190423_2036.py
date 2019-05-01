# Generated by Django 2.2 on 2019-04-23 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0003_auto_20190423_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Eshop.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_toal',
            field=models.DecimalField(decimal_places=2, default=10.99, max_digits=100),
        ),
    ]
