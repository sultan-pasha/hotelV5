# Generated by Django 3.2.2 on 2021-07-12 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_rem_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rem',
            options={'ordering': ['-rerate'], 'verbose_name': 'rate'},
        ),
    ]
