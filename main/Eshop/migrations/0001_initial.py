# Generated by Django 2.2 on 2019-04-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soort', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=200)),
                ('prijs', models.DecimalField(decimal_places=2, max_digits=100)),
                ('btw', models.DecimalField(decimal_places=2, max_digits=100)),
                ('merk', models.CharField(max_length=201)),
                ('image', models.ImageField(upload_to='images/')),
                ('productCount', models.IntegerField(default=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Eshop.Category')),
            ],
        ),
    ]