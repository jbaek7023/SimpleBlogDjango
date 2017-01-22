from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def home(request):
    posts = models.Post.objects.order_by('-pub_date')
    return render(request, 'posts/home.html', {'posts':posts})


def post_detail(request, post_id):
    # post = models.Post.objects.get(pk=post_id)
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/permanent.html', {'post': post })
