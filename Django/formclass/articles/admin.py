from django.contrib import admin
from .models import Article

list_display = ('pk', 'title', 'created_at', 'updated_at')

admin.site.register(Article)
