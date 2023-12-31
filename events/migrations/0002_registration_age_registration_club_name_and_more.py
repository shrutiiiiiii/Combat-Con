# Generated by Django 4.1.7 on 2023-03-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='age',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='registration',
            name='club_name',
            field=models.CharField(default='UNK', max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='contact_number',
            field=models.CharField(default='eg. 3896346734', max_length=20),
        ),
        migrations.AddField(
            model_name='registration',
            name='fighting_style',
            field=models.CharField(default='UNK', max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='MALE', max_length=30),
        ),
        migrations.AddField(
            model_name='registration',
            name='height',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=4),
        ),
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(default='FirstName MiddleName LastName', max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=40, max_digits=4),
        ),
        migrations.AddField(
            model_name='registration',
            name='weight_category',
            field=models.CharField(choices=[('Straw Weight', 'Straw Weight'), ('Fly Weight', 'Fly Weight'), ('Bantam Weight', 'Bantam Weight')], default='FLY WEIGHT', max_length=30),
        ),
    ]
