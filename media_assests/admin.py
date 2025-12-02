from django.contrib import admin
from .models import MediaAssests

# Register your models here.
@admin.register(MediaAssests)
class MediaAssestsAdmin(admin.ModelAdmin):
    list_display = ('title','category','uploaded_by','is_public','views_count','created_at')
    list_filter = ('category','is_public','created_at')
    search_fields = ('title','description','uploaded_by__username')
    readonly_fields = ('created_at','updated_at','views_count')
    date_hierarchy = ('created_at') #data ordering for admin 
