# Generated by Django 5.1.5 on 2025-01-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderstatus_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
