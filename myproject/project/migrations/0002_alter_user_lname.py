# Generated by Django 4.1.3 on 2022-11-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия'),
        ),
    ]