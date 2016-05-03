from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

def upload_location(instance, filename):
    return '%s/%s' %(instance.id, filename)
# Create your models here.
class Houses(models.Model):
    picture = models.ImageField(upload_to= upload_location,
            null=True, 
            blank=True, 
            height_field='height_field', 
            width_field='width_field')
    height_field = models.IntegerField(default=100)
    width_field = models.IntegerField(default=100)
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

    def get_absolute_url(self):
        return reverse("post", kwargs={'pk': self.pk})

# def  create_slug(instance,new_slug = None):
#     slug = slugify(instance.name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Houses.objects.filter(slug=slug).order_by(id)
#     exists = qs.exists()

#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_receiver(sender, instance, *args, **kwargs): 
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_receiver, sender=Houses)