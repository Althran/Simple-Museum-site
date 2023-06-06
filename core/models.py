from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    slug = models.SlugField(max_length=256)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='b_posts')
    image = models.ImageField(upload_to='posts/')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.post_detail', args=[self.id])


class Item(models.Model):
    title = models.CharField(max_length=56)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.item_detail', args=[self.id])


class Contest(models.Model):
    title = models.CharField(max_length=56)
    body = models.TextField()
    slug = models.SlugField(max_length=256)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.contest_detail', args=[self.id])
