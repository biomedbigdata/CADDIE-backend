# Generated by Django 3.0.5 on 2022-02-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddie', '0023_cancernet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancernet',
            name='combination_formation',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='cancernet',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='cancernet',
            name='notes',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='cancernet',
            name='target',
            field=models.CharField(default='', max_length=500),
        ),
    ]
