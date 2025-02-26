from django.http import HttpResponse
from django.template import loader

from category.models import Category


def index(request):
    template = loader.get_template("home.html")
    context = {
        "categories": Category.objects.order_by("name"),
    }
    return HttpResponse(template.render(context, request))
