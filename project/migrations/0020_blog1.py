# Generated by Django 3.0.4 on 2020-03-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_delete_blog1'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('blog', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
