from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published','post_categories')
    ordering=('published','author')
    search_fields=('title',)
    date_hierarchy='published'
    list_filter=('author__username',)
    
    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    
    post_categories.short_description='Categorias'
        
        
    
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    
admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)
