# Generated by Django 2.1.2 on 2018-11-03 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Cin', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
