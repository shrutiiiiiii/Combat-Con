from django.db import models
from django.contrib.auth.models import AbstractUser
from Combat_conog import settings
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator

class MyUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifier
    for authentication instead of email.
    """

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must have a username'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

class MyUser(AbstractUser):
    objects = MyUserManager()
    is_athlete=models.BooleanField(default=True)
    is_host=models.BooleanField(default=False)
    first_name = None
    last_name = None

    def __str__(self):
        return self.username

class Athlete(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    WEIGHT_CATEGORY_CHOICES = (
        ('Strawweight', 'Strawweight'),
        ('Flyweight', 'Flyweight'),
        ('Bantamweight', 'Bantamweight'),
        ('Featherweight', 'Featherweight'), 
        ('Lightweight', 'Lightweight'),
        ('Super Lightweight', 'Super Lightweight'),
        ('Welterweight', 'Welterweight'),
        ('Super Welterweight', 'Super Welterweight'), 
        ('Middleweight', 'Middleweight'),
        ('Super Middleweight', 'Super Middleweight'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='N/S')
    profile_picture = models.ImageField(upload_to='athlete_pics/', null=True, blank=True, default='C:\SHRUTI\SEM_6\PROJECT\Combat_conog\athlete_pics\default_img.png')
    contact_number = models.IntegerField(validators=[MaxValueValidator(9999999999)], default='9843029462')
    date_of_birth = models.DateField(default='2011-1-1')
    age = models.IntegerField(default=12)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.DecimalField(max_digits=4, decimal_places=2, default=4)
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=40)
    weight_category = models.CharField(max_length=20, choices=WEIGHT_CATEGORY_CHOICES)
    fighting_style = models.CharField(max_length=100, default='UNK')
    club_name = models.CharField(max_length=100, default='UNK')
    coach_name = models.CharField(max_length=100, default='UNK')
    record = models.CharField(max_length=100, default='UNK')

    def __str__(self):
        return self.user.username

class Host(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host')
    name = models.CharField(max_length=100, default='N/S')
    contact_number = models.IntegerField(validators=[MaxValueValidator(9999999999)], default='9843029462')
    organization_name = models.CharField(max_length=100)
    events_hosted = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username


# Create your models here.
