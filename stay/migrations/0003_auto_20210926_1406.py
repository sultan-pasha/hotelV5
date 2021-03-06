# Generated by Django 3.2.2 on 2021-09-26 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_roomm_roday'),
        ('stay', '0002_alter_stay_ipuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='brom',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.roomm', verbose_name='room'),
        ),
        migrations.AlterField(
            model_name='stay',
            name='stay',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='long stay'),
        ),
    ]
