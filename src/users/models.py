from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def save(self, **kwargs):
        super().save()
        size = (320, 320)
        img = Image.open(self.image.path)
        img.thumbnail(size, Image.ANTIALIAS)
        thumb = ImageOps.fit(img, size, Image.ANTIALIAS)
        thumb.save(self.image.path)
