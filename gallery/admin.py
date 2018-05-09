from django.contrib import admin
from .models import Project, Picture, Video
from django.utils.html import mark_safe

# Register your models here.


class PictureInline(admin.TabularInline):
    model = Picture

    def get_screenshot(self, obj):
        if obj.screenshot:
            return mark_safe('<img src="{url}" alt="Здесь должна быть картинка" height="250" width="250"/>'.format(
                url=obj.screenshot.url
            ))
        return mark_safe('<img src="" alt="Здесь должна быть картинка" height="250" width="250"/>')

    get_screenshot.short_description = 'Изображение'
    readonly_fields = ['get_screenshot']

class VideoInline(admin.TabularInline):
    model = Video


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline,
        VideoInline,
    ]
    list_filter = ['created', 'title']
    search_fields = ['title', 'description', 'url']
    prepopulated_fields = {"slug_title": ("title",)}
    list_display = (
        'title',
        'url',
        'created',
        'category'
    )


admin.site.register(Project, ProjectAdmin)