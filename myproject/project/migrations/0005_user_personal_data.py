# Generated by Django 4.1.3 on 2022-11-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='personal_data',
            field=models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных'),
        ),
    ]