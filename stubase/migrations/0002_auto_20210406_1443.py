# Generated by Django 3.1.7 on 2021-04-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stubase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('classandsec', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='XC',
        ),
    ]