# Generated by Django 5.1.4 on 2024-12-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_connections',
            field=models.ManyToManyField(blank=True, related_name='followers', to='cadastro.profile'),
        ),
    ]