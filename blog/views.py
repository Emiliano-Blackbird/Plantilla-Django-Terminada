from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post


# Vistas generales de la app
def blog_list(request):
    all_posts = Post.objects.all()  # Todos los posts de la base de datos
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/blog_list.html', context)


class BlogListView(ListView):  # Vista basada en clase (CCBV)
    model = Post
    template_name = 'blog/blog_list_ccbv.html'  # Nombre del template
    context_object_name = 'posts'


def blog_detail(request, id):
    post = Post.objects.get(pk=id)  # Obtener el post por su id
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)
