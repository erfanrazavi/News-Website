from django.contrib import admin
from index.models import Contact
# Register your models here.


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ["fullname" , "subject", "email"]
    
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    search_fields = ["email"]
    