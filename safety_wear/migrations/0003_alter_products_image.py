# Generated by Django 3.2.16 on 2023-02-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_wear', '0002_auto_20230220_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]