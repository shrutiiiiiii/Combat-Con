from django.db import models
from Combat_conog import settings
from users.models import Athlete, Host


class Event(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='hosted_events')
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    last_reg_date = models.DateField()
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2)
    prize = models.DecimalField(max_digits=8, decimal_places=2)
    contact_no = models.CharField(max_length=20)
    ig_handle = models.CharField(max_length=100, null=True, blank=True)
    fb_handle = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    registered_athletes = models.ManyToManyField(Athlete, through='Registration', related_name='registrations')

    def __str__(self):
        return self.title
    

class Registration(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    age = models.IntegerField(default=12)
    gender = models.CharField(max_length=30, choices=Athlete.GENDER_CHOICES)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    weight_category = models.CharField(max_length=30, choices=Athlete.WEIGHT_CATEGORY_CHOICES)
    fighting_style = models.CharField(max_length=100)
    club_name = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.athlete.user.username} registered for {self.event.title}'
