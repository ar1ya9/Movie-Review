from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=300)
    director=models.CharField(max_length=300)
    cast=models.CharField(max_length=800)
    description=models.TextField(max_length=5000)
    release=models.DateField()
    language=models.CharField(max_length=50,null=True)
    arating=models.FloatField(default=0)
    image = models.URLField(default=None, null=True)


    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
class MovieReview(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
