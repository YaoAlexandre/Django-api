# Generated by Django 4.1.5 on 2023-03-10 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('essivivi_api', '0009_rename_stock_livre_livraison_stock_livrer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usereau',
            old_name='QteStock',
            new_name='qteStock',
        ),
    ]
