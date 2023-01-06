# Generated by Django 4.1.5 on 2023-01-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvestmentCdi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentcdi',
            name='current_value',
            field=models.DecimalField(decimal_places=2, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='investmentcdi',
            name='yield_value',
            field=models.DecimalField(decimal_places=2, max_digits=17, null=True),
        ),
    ]