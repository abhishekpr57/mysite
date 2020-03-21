# Generated by Django 3.0.4 on 2020-03-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=200)),
                ('Premium', models.BooleanField(default=False)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('about', models.TextField()),
            ],
        ),
    ]