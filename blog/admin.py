from django.contrib import admin

# Register your models here.
from .models import Post, Commentaire
admin.site.register(Post)
admin.site.register(Commentaire)
