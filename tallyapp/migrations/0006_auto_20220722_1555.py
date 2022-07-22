# Generated by Django 3.1.5 on 2022-07-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0005_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='first_unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='formal_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='second_unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='symbol',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
