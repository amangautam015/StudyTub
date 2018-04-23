from django.contrib import admin
from .models import Course,Chapter,Department,Material


class Filter(admin.ModelAdmin):
    list_display = ('title','department',)
    list_filter = ('department',)
    search_fields = ('title',)
    ordering = ('title',)
class Filter1(admin.ModelAdmin):
    list_display = ('chapter_title','course',)
    list_filter = ('course',)
    search_fields = ('chapter_title',)
    ordering = ('chapter_title',)
class Filter2(admin.ModelAdmin):
    list_display = ('name','chapter',)
    list_filter = ('chapter',)
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Department)
admin.site.register(Material,Filter2)
admin.site.register(Course,Filter)
admin.site.register(Chapter,Filter1)
