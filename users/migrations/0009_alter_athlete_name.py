# Generated by Django 4.1.7 on 2023-04-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_host_events_hosted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
