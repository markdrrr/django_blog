from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment, Categories, HashTag, Mark

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'parent', 'tree_id', 'level')
    fields = ('name', 'parent')

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categories,CategoryMPTTModelAdmin)
admin.site.register(HashTag)
admin.site.register(Mark)

