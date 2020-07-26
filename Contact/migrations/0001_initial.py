# Generated by Django 3.0.8 on 2020-07-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField(max_length=5000)),
                ('User_Ip', models.GenericIPAddressField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
            ],
            options={
                'db_table': 'Contact Us',
            },
        ),
    ]
