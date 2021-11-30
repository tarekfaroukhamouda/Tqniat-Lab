# Generated by Django 3.2.9 on 2021-11-30 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenityName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('providerName', models.CharField(max_length=200)),
                ('seprately', models.IntegerField(choices=[(1, 'Array Of String'), (2, 'comma')])),
                ('ratetype', models.IntegerField(choices=[(1, 'stars'), (2, 'numbers')])),
                ('HasDiscount', models.BooleanField(default=False)),
                ('priceType', models.IntegerField(choices=[(2, 'Price'), (1, 'Fare')])),
            ],
        ),
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelName', models.CharField(max_length=200)),
                ('rate', models.IntegerField()),
                ('price', models.FloatField()),
                ('amenities', models.ManyToManyField(to='apis.amenities')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotelsCity', to='apis.cities')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='apis.providers')),
            ],
        ),
    ]
