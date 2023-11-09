from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from forum.models import Comment, Post


def index(request):
    return HttpResponse('<html><body>Our first response</body></html>')


class PostListView(ListView):
    model = Post
    context_object_name = 'post_data'

    def get_queryset(self):
        self.queryset = Post.objects.all()
        if self.kwargs.get('year'):
            self.queryset = self.queryset.filter(created_at__year=self.kwargs['year'])
        if self.kwargs.get('month'):
            self.queryset = self.queryset.filter(created_at__month=self.kwargs['month'])
        return self.queryset

    def render_to_response(self, context, **response_kwargs):
        posts = ''
        for post in context['post_data']:
            posts += f'<li>{post.title}</li>'
        return HttpResponse(f'<html><body><ul>{posts}</ul></body></html>')


class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        post = context.get('object')
        return HttpResponse(f'<html><body><ul>'
                            f'<li>Title: {post.title}</li>'
                            f'<li>Body: {post.body}</li>'
                            f'<li>User: {post.user.first_name}</li>'
                            f'</ul></body></html>')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment_data'

    def get_queryset(self):
        self.queryset = Comment.objects.filter(post__id=self.kwargs['post_id'])
        return self.queryset

    def render_to_response(self, context, **response_kwargs):
        comments = ''
        for comment in context['comment_data']:
            comments += f'<li>{comment.body}</li>'
        return HttpResponse(f'<html><body><ul>{comments}</ul></body></html>')
