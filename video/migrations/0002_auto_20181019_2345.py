# Generated by Django 2.1.2 on 2018-10-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]