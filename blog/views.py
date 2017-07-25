from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category


class BlogMixinView(object):
    def get_context_data(self, *args, **kwargs):

        context = super(BlogMixinView, self)\
            .get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['current_page'] = 'blog'

        return context


class PostList(BlogMixinView, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(published=True)


class PostDetailView(BlogMixinView, DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_queryset(self, *args, **kwargs):
        queryset = super(PostDetailView, self).get_queryset(*args, **kwargs)

        if not self.request.user.is_authenticated:
            queryset = queryset.filter(published=True)

        return queryset


class CategoryListView(BlogMixinView, ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)

        context['category'] = self.category

        return context

    def get_queryset(self, *args, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])

        posts = Post.objects.filter(categories=self.category, published=True)

        return posts
