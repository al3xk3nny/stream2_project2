# Generated by Django 2.0.8 on 2018-11-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='marketer', max_length=10),
        ),
    ]
