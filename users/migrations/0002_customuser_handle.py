# Generated by Django 3.0.5 on 2020-04-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='handle',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
