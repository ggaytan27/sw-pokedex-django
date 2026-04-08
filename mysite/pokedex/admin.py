from django.contrib import admin

# Register your models here.
from .models import Pokemon #Adding models to the admin page

admin.site.register(Pokemon) #Registering the Pokemon model to the admin page