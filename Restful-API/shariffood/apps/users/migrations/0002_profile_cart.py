# Generated by Django 3.0.2 on 2020-01-29 16:49

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
