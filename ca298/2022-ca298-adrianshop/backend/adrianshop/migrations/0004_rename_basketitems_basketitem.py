# Generated by Django 4.0.1 on 2022-02-08 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adrianshop', '0003_product_product_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BasketItems',
            new_name='BasketItem',
        ),
    ]