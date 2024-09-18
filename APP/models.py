from django.db import models


class upload(models.Model):
    images = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now_add=True)