from django.contrib import admin
from .models import BlogPost, Category, Tag, AuthorProfile, Gallery, Event

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "category", "created_at", "published")
    list_filter = ("category", "published", "created_at")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(AuthorProfile)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("event", "media_type", "created_at")
    list_filter = ("media_type", "created_at")


admin.site.register(Event)
