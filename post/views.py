from django.shortcuts import render, redirect, get_object_or_404

from category.models import Category
from .models import PostImage, Post
from .forms import PostForm, PostImageFormSet


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def category_post_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_post_list.html', {'category': category, 'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        formset = PostImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

        if form.is_valid() and formset.is_valid():
            post = form.save()
            for image_form in formset:
                if image_form.cleaned_data:
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('index')
    else:
        form = PostForm()
        formset = PostImageFormSet(queryset=PostImage.objects.none())

    return render(request, 'add_post.html', {'form': form, 'formset': formset})
