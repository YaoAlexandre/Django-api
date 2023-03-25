# Generated by Django 4.1.5 on 2023-03-10 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('essivivi_api', '0008_remove_eau_user_eau_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livraison',
            old_name='stock_livre',
            new_name='stock_livrer',
        ),
        migrations.RemoveField(
            model_name='eau',
            name='statut',
        ),
        migrations.RemoveField(
            model_name='eau',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='eau',
            name='volume',
        ),
        migrations.CreateModel(
            name='UserEau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QteStock', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='essivivi_api.eau')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', '-created_at'],
            },
        ),
    ]