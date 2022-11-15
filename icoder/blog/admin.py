from django.contrib import admin
from .models import post,comment
#Register your models here.
admin.site.register((comment))
@admin.register(post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)