# Generated by Django 3.1.3 on 2021-05-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20210528_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('myAge', models.IntegerField()),
            ],
        ),
    ]
