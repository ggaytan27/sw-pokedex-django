from django.contrib import admin
# Register your models here.
from .models import Pokemon #Adding models to the admin page

#(same function that the dercorator @admin.register(Pokemon))
#admin.site.register(Pokemon) #Registering the Pokemon model to the admin page

@admin.register(Pokemon) #Using the decorator to register the Pokemon model to the admin page
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type', 'status', 'updated' )
    list_filter = ('status', 'type')
    search_fields = ('name', 'type')
    prepopulated_fields = {'slug': ('name',)} #Automatically fill the slug field with the name field
    #raw_id_fields
    date_hierarchy = 'update' #Add a date hierarchy to the admin page based on the update field
    ordering = ('-update',) #Order the pokemons by the date they were updated