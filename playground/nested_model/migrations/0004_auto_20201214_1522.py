# Generated by Django 3.1.4 on 2020-12-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nested_model', '0003_auto_20201214_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='point',
            name='y',
            field=models.FloatField(),
        ),
    ]