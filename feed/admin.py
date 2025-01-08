from django.contrib import admin

# Register your models here.
from .models import Post, Curtida, Iteracao

admin.site.register(Post)
admin.site.register(Curtida)
admin.site.register(Iteracao)
