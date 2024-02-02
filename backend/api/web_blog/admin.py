from django.contrib import admin
from .models import BlogPost , Comment



# BLOG
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content','modifyed_by')  # Customize the fields displayed in the list view
    # search_fields = ('field1', 'field2')  # Add search functionality for specified fields
    # list_filter = ('field3',)  # Add filters for specified fields

admin.site.register(BlogPost, BlogPostAdmin)


# COMMENT 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content','created')  # Customize the fields displayed in the list view
    # search_fields = ('field1', 'field2')  # Add search functionality for specified fields
    # list_filter = ('field3',)  # Add filters for specified fields

admin.site.register(Comment, CommentAdmin)


