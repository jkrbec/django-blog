from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random

default_img = ['default.jpg', 'default2.jpg', 'default3.jpg', 'default4.jpg']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Check if the profile is new (i.e. being created)
        if not self.pk:
            # Choose a random image from the list and assign it to the image field
            self.image.name = random.choice(default_img)
        super().save(*args, **kwargs)

        # Resize the image if it is larger than 300x300
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# import random

# default_img = ['default.jpg', 'default2.jpg', 'default3.jpg', 'default4.jpg']

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default=random.choice(default_img), upload_to='profile_pics')
#     #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)


