# Generated by Django 3.1.3 on 2021-05-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choicetext', models.CharField(max_length=100)),
                ('questiongrade', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chocies', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
    ]
