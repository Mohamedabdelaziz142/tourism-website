from django.db import models
from django.contrib.auth.models import User
from PIL import Image,ExifTags


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
       return f'{self.user.username} profile'
    
    def save(self):

        super().save()

        img = Image.open(self.image.path)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
            if hasattr(img, '_getexif') and isinstance(img._getexif(), dict):
              exif_data = img._getexif()
              if exif_data is not None:
                exif_orientation = exif_data.get(orientation)
                if exif_orientation is not None:
                    if exif_orientation == 3:
                        img = img.rotate(180, expand=True)
                    elif exif_orientation == 6:
                        img = img.rotate(270, expand=True)
                    elif exif_orientation == 8:
                        img = img.rotate(90, expand=True)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)