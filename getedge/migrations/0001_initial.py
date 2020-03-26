# Generated by Django 3.0.4 on 2020-03-25 16:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patientregistration',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-username'],
            },
        ),
        migrations.CreateModel(
            name='Patientdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.FloatField()),
                ('spo2', models.FloatField()),
                ('blood_pressure', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getedge.Patientregistration')),
            ],
        ),
    ]
