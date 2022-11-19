# Generated by Django 4.1.3 on 2022-11-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_account_addr_account_mobno'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrders',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('time', models.IntegerField()),
                ('food', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('paymentMethod', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FinishedOrders',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('timetoorder', models.IntegerField()),
                ('food', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('hotel', models.CharField(max_length=40)),
                ('food', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
                ('approxTime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelOwner',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=30)),
                ('hotelName', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=30)),
                ('addr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('amountType', models.CharField(max_length=30)),
                ('pending', models.IntegerField()),
                ('wallet', models.IntegerField()),
            ],
        ),
    ]
