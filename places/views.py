from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Destination

# Create your views here.
@cache_page(60 * 15)
def index(req):
    dests= Destination.objects.all()
    return render(req,"index.html",{'dests':dests})