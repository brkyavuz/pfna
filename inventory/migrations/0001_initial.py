# Generated by Django 4.0.3 on 2022-03-15 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('platform', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('country', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('device_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('device_type', models.CharField(max_length=16)),
                ('hostname', models.GenericIPAddressField(unique=True)),
                ('platform', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('port', models.IntegerField()),
                ('country', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=16)),
                ('groups', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.group')),
            ],
        ),
    ]
