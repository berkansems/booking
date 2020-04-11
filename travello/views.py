from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):

    offers=Destination.objects.all()
    context={'offers':offers}

    return render(request,"pages/index.html",context)


def signin(request):



    return render(request,"pages/signin.html")