from django.contrib import admin
from .models import Category, Post, Rating, Comment, Settings, Banner

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Settings)
admin.site.register(Banner)
