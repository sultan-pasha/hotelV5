# Generated by Django 3.2.2 on 2021-09-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0009_alter_stay_totprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='totprice',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='total price'),
        ),
    ]
