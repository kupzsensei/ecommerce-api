# Generated by Django 5.1.5 on 2025-01-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0005_shippingaddress_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(to='cart.cart'),
        ),
    ]
