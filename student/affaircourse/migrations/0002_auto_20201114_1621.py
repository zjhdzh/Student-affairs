# Generated by Django 3.1.2 on 2020-11-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affaircourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
