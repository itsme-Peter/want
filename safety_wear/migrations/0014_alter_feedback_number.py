# Generated by Django 3.2.16 on 2023-05-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safety_wear', '0013_feedback_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='number',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
    ]
