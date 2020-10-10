from django.contrib import admin
from .models import ReLearn # add this
#testing 

class ReLearnAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(ReLearn, ReLearnAdmin) # add this