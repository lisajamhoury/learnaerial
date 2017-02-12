from django_summernote.widgets import SummernoteWidget


from django.contrib import admin
from django.forms import ModelForm

from .models import Post, Author, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = (
        'title',
        'author',
        'published'
    )


class CategoryAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)

