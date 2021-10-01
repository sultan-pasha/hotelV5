# Generated by Django 3.2.2 on 2021-09-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0014_alter_stay_options'),
        ('order', '0004_auto_20210927_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bdetail',
        ),
        migrations.AddField(
            model_name='order',
            name='bdetail',
            field=models.ManyToManyField(to='stay.stay', verbose_name='book detail'),
        ),
    ]