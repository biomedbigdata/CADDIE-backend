# Generated by Django 3.0.5 on 2020-10-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddie', '0005_expressionlevel_tissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='is_nutraceutical',
            field=models.BooleanField(default=False),
        ),
    ]