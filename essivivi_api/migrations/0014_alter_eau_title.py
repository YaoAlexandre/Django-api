# Generated by Django 4.1.5 on 2023-03-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essivivi_api', '0013_agent_gerant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eau',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
