# Generated by Django 3.0.5 on 2022-02-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddie', '0024_auto_20220224_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancernet',
            name='cancer_type_long',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='cancernet',
            name='notes',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='cancernet',
            name='target',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
