# Generated by Django 4.1.5 on 2023-02-28 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('essivivi_api', '0005_delete_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbr_eaux', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='essivivi_api.produit')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', '-created_at'],
            },
        ),
        migrations.AddField(
            model_name='produit',
            name='user',
            field=models.ManyToManyField(through='essivivi_api.Agent', to=settings.AUTH_USER_MODEL),
        ),
    ]
