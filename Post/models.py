from django.db import models
from django.utils import timezone

from django.urls import reverse

from autoslug import AutoSlugField
from taggit.managers import TaggableManager

from django import template

register = template.Library()

def custom_slugify(value):
    return value.replace(' ','-')


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),)

    title = models.CharField(max_length=255)
    body = models.TextField()

    slug = AutoSlugField(max_length=50, unique_for_date='publish', populate_from='title', 
                        slugify=custom_slugify)

    tags = TaggableManager()

    publish = models.DateTimeField(default=timezone.now)
    date    = models.DateField(auto_now_add=True)
    status  = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')

    image = models.ImageField(upload_to='model/img/', blank=True, null=True)
    image_alt = models.CharField(max_length = 255, default= "", blank=True)

    class Meta():
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    @register.simple_tag 
    def has_image_(self):
        if self.image:
            return True
        return False

    def get_absolute_url(self):
        return reverse('post:post_detail',args=[self.publish.year,self.publish.month,self.publish.day, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    author = models.CharField(max_length=255)
    body = models.TextField()

    date = models.DateField(default=timezone.now)

    # En caso de estar respondiendo a un commentario, esta variable es la clave del mismo
    comment_parent = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body
    