# Generated by Django 3.2.11 on 2022-01-20 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('mobile', models.CharField(max_length=16, verbose_name='Mobile')),
                ('nationality', models.CharField(max_length=128)),
                ('identification_type', models.CharField(choices=[('Passport', 'Passport'), ('ID', 'ID')], max_length=128)),
                ('identification_id', models.CharField(max_length=128, verbose_name='Identification ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32)),
                ('result_time', models.DateTimeField()),
                ('result', models.CharField(choices=[('Negative', 'Negative'), ('Positive', 'Positive')], max_length=32)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]