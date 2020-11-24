from django.contrib import admin
from .models import lenders,catagories,books

# Register your models here.

admin.site.register(lenders)
admin.site.register(catagories)
admin.site.register(books)
