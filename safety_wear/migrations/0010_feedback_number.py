# Generated by Django 3.2.16 on 2023-05-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_wear', '0009_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='number',
            field=models.CharField(default='0712345678', max_length=100000),
        ),
    ]
