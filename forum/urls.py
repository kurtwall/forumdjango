from django.urls import path, re_path
from .views import index, PostDetailView, PostListView

urlpatterns = [
    # ex: /forum/
    path('', index, name='index'),

    # ex: /forum/5/
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    #
    # # ex: /forum/5/comment/
    # path('<int:post_id>/comment/', 'views.comment', name='comment'),
    #
    # ex: /posts/2023/
    re_path(r'^posts/(?P<year>[0-9]{4})/$', PostListView.as_view(), name='by_year'),

    # ex /forum/posts/2023/03/
    re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', PostListView.as_view(), name='by_month'),
    #
    # # ex /forum/posts/2023/03/post-slug/
    # re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w+])$', 'views.post_detail', name='slug_detail'),
]
