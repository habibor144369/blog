# Generated by Django 3.0.5 on 2021-03-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='key',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]