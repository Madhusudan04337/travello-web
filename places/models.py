from django.db import models
from cloudinary.models import CloudinaryField

class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = CloudinaryField('image')  # ✅ Cloudinary
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name