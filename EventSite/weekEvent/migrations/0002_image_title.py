# Generated by Django 2.2.3 on 2020-12-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekEvent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='None', max_length=300),
        ),
    ]
