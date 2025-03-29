from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from category.models import Category
from post.models import Post


def index(request):
    template = loader.get_template("home.html")
    context = {
        "categories": Category.objects.order_by("name"),
        "posts": Post.objects.all()
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                pass
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
