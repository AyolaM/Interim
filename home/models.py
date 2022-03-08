from django.db import models

# Create your models here.
class Interim(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # parameter allows automatic time captre
    created = models.DateTimeField(auto_now_add=True)
