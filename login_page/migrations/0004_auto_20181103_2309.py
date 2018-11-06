# Generated by Django 2.1.2 on 2018-11-03 23:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0003_auto_20181103_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8', regex='^.{8}$')]),
        ),
    ]