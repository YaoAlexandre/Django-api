# Generated by Django 4.1.5 on 2023-02-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essivivi_api', '0003_alter_agent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='eau',
        ),
        migrations.AddField(
            model_name='agent',
            name='eau',
            field=models.ManyToManyField(to='essivivi_api.eau'),
        ),
    ]