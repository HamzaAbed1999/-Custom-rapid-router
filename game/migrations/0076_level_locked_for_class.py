# Generated by Django 3.2.15 on 2022-10-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0030_add_maintenance_banner'),
        ('game', '0075_level_48_houses'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='locked_for_class',
            field=models.ManyToManyField(blank=True, related_name='locked_levels', to='common.Class'),
        ),
    ]
