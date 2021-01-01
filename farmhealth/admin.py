from django.contrib import admin
from .models import  tomato_plant, apple_plant, grapes_plant, corn_plant 
# Register your models here.


admin.site.register(tomato_plant)
admin.site.register(apple_plant)
admin.site.register(grapes_plant)
admin.site.register(corn_plant)
