# Generated by Django 4.0.3 on 2022-03-15 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_device_name_host_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('device_type', models.CharField(max_length=16)),
                ('country', models.CharField(blank=True, max_length=16, null=True)),
                ('city', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='host',
            name='city',
        ),
        migrations.RemoveField(
            model_name='host',
            name='country',
        ),
        migrations.RemoveField(
            model_name='host',
            name='device_type',
        ),
        migrations.AddField(
            model_name='host',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.data'),
        ),
    ]
