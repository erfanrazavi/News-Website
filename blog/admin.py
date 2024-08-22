from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ["title" , "status", "created_date" ,  "counted_views" ,"image"]
    
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    search_fields = ["content"]
    list_editable = ("status",)
    