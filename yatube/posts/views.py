from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from typing import Any, Dict
from django.core.paginator import Paginator


def index(request):
    """Главная страница."""
    posts = Post.objects.order_by('-pub_date')
    p = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    title: str = 'Последние обновления на сайте.'
    context: Dict[str, Any] = {
        'posts': posts,
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Страницы сообществ."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')
    context: Dict[str, Any] = {
        'title': group.title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
