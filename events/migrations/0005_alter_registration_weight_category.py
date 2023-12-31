# Generated by Django 4.1.7 on 2023-04-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_host_alter_registration_athlete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='weight_category',
            field=models.CharField(choices=[('Strawweight', 'Strawweight'), ('Flyweight', 'Flyweight'), ('Bantamweight', 'Bantamweight'), ('Featherweight', 'Featherweight'), ('Lightweight', 'Lightweight'), ('Super Lightweight', 'Super Lightweight'), ('Welterweight', 'Welterweight'), ('Super Welterweight', 'Super Welterweight'), ('Middleweight', 'Middleweight'), ('Super Middleweight', 'Super Middleweight')], max_length=30),
        ),
    ]
