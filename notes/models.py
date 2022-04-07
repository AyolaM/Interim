from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # parameter allows automatic time capture
    created = models.DateTimeField(auto_now_add=True)
