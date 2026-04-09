from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Models
class CaughtManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='caught')

class Pokemon(models.Model):
    STATUS_CHOICES = [
        ('caught', 'Caught'),
        ('seen','Seen'),
        ('not_seen', 'Not Seen'),
    ]
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)
    type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_seen')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    # To order the pokemons by the date they were created
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'

    def __str__(self):
        return self.name
    
    objects = models.Manager()
    caught = CaughtManager()