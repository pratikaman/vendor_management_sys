# Generated by Django 5.0.4 on 2024-05-04 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management', '0005_alter_purchaseorder_quality_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]