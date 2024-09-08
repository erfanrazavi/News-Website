from django.contrib import admin
from blog.models import Post , Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ["title" , "status", "created_date" ,  "counted_views" ,"image"]
    
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    search_fields = ["content"]
    list_editable = ("status",)
    summernote_fields = 'content'

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ["name" ]
    
    