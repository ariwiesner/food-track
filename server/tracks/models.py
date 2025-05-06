from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=10, blank=False)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)


class Hashtag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='places/', blank=True, null=True)
    address = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    category = models.CharField(max_length=20)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    added_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='added_places')
    is_visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='ratings')
    reporter = models.ForeignKey('User', on_delete=models.CASCADE, related_name='ratings')
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField()

    
    def __str__(self):
        return f"{self.reporter.username} - {self.place.name} ({self.points})"


class ToVisitPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    heard_from = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)


class SharedAccess(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=True)
    shared_at = models.DateTimeField(auto_now_add=True)