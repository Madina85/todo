# Generated by Django 3.2.4 on 2021-08-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tomeet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal_for_month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.TextField(verbose_name='Цели')),
                ('month', models.CharField(max_length=50)),
                ('difficulty', models.BooleanField(default=False)),
                ('reason_for_goal', models.TextField(verbose_name='Причина')),
            ],
        ),
    ]
