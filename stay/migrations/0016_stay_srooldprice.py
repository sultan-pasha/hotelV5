# Generated by Django 3.2.2 on 2021-09-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0015_stay_sroprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='srooldprice',
            field=models.IntegerField(blank=True, null=True, verbose_name='previous rom price'),
        ),
    ]