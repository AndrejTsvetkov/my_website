from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from model_utils import FieldTracker
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tracker = FieldTracker()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        if self.tracker.has_changed('image'):
            if os.path.isfile(self.tracker.previous('image').path):
                os.remove(self.tracker.previous('image').path)
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
