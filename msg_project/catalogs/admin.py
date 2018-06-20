from django.contrib import admin
from . import models


#class PostAdmin(admin.ModelAdmin):
    #inlines = [ CommentInline, ]

# Register your models here.
admin.site.register(models.Catalog)