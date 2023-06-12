from django.http import HttpResponse
from django.shortcuts import render


def docs_home(request):
    return render(request, "django_documents/home.html", context={})


def docs_list(request):
    return HttpResponse("docs_list")


def docs_detail(request):
    return HttpResponse("docs_detail")


def docs_public(request):
    return HttpResponse("docs_public")
