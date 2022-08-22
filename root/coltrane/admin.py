from django.contrib import admin
from .models import Category, Entry, Link

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, BlogPostAdmin)
admin.site.register(Entry, BlogPostAdmin)
admin.site.register(Link, BlogPostAdmin)