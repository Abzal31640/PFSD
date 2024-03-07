# Generated by Django 5.0 on 2024-02-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_admin_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('phno', models.CharField(max_length=30, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'register_table',
            },
        ),
    ]
