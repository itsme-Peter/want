# Generated by Django 3.2.16 on 2023-03-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_wear', '0007_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]