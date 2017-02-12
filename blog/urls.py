from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='blog_index'),
    url(r'^categories/(?P<slug>[-\w]+)/$', views.CategoryListView.as_view(), name='blog_category'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='blog_post_detail'),
]
