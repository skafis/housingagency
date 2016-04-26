from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Houses(models.Model):
    picture = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=140)
    location = models.CharField(max_length=200)
    price =  models.DecimalField(max_digits=6, decimal_places=2)
    bedrooms = models.IntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name