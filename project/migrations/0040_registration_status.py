# Generated by Django 3.0.4 on 2020-03-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0039_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]