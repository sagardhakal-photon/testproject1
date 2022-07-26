# Generated by Django 4.0.6 on 2022-07-25 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20, verbose_name='Title')),
                ('Alubm_ID', models.IntegerField()),
                ('Copyright_Data', models.CharField(max_length=100)),
                ('Format', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Full_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_Num', models.IntegerField(verbose_name='Phone Number:')),
                ('City', models.CharField(max_length=20, verbose_name='City Name')),
                ('Area', models.CharField(max_length=20, verbose_name='Area')),
                ('Street', models.CharField(max_length=20, verbose_name='Street')),
                ('House_Num', models.CharField(max_length=20, verbose_name='House Number')),
            ],
            options={
                'db_table': 'full_address',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instrument_ID', models.IntegerField()),
                ('Music_Key', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'instrument',
            },
        ),
        migrations.CreateModel(
            name='Instrument_Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_Sn', models.IntegerField()),
                ('Instrument_ID', models.IntegerField()),
            ],
            options={
                'db_table': 'instrument_player',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song_ID', models.IntegerField()),
                ('M_Sn', models.IntegerField()),
            ],
            options={
                'db_table': 'performance',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Song_ID', models.IntegerField()),
                ('Author', models.CharField(max_length=100)),
                ('Album_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicdatab.album')),
            ],
            options={
                'db_table': 'song',
            },
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_Sn', models.IntegerField()),
                ('First_Name', models.CharField(max_length=100)),
                ('Mid_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Phone_Num', models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='musicdatab.full_address')),
            ],
            options={
                'db_table': 'musician',
            },
        ),
    ]
