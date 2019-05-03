from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
