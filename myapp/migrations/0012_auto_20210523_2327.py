# Generated by Django 3.0.5 on 2021-05-24 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_adidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adidas',
            name='talle',
            field=models.CharField(max_length=128, verbose_name='Talle'),
        ),
    ]
