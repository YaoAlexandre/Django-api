# Generated by Django 4.1.5 on 2023-02-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essivivi_api', '0002_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
