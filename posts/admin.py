#Django
from django.contrib import admin

#Local
from posts.models import Post
from django.contrib.auth.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""

    list_display = ('pk', 'title', 'user', 'created_at')

