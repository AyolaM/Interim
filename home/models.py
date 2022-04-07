from django.db import models

# Create your models here.


class Interim(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # parameter allows automatic time captre
    created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    # parameter allows automatic time captre
    created = models.DateTimeField(auto_now_add=True)

