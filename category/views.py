from django.http import HttpResponse
from django.template import loader

from category.models import Category
from post.models import Post


def index(request):
    template = loader.get_template("home.html")
    context = {
        "categories": Category.objects.order_by("name"),
        "posts": Post.objects.all()
    }
    return HttpResponse(template.render(context, request))
