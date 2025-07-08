from django.db import models


# Simple model for photos
class Photo(models.Model):
    title = models.CharField(max_length=100)  # Photo title
    image = models.ImageField(upload_to="photos/")  # Upload image
    likes = models.PositiveIntegerField(default=0)  # Like count
    dislikes = models.PositiveIntegerField(default=0)  # Dislike count

    def __str__(self):
        return self.title
