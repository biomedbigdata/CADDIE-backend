# Generated by Django 3.0.5 on 2022-03-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddie', '0027_empiricalnodedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='in_ctrpv2',
            field=models.BooleanField(default=False),
        )
    ]