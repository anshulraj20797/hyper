# Generated by Django 3.0.6 on 2022-03-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('checked', models.BooleanField()),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
