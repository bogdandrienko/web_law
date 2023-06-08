from django.http import HttpResponse
from django.shortcuts import render
from django_app import models


def home(request):
    #
    data = [{"id": x, "name": f"Алема {x}"} for x in range(1, 100 + 1)]
    return render(request, "django_app/home.html", context={"peoples": data})


# todo REQUESTS ###############################################
def get_requests(request):
    # вернуть все запросы

    # todo выборка
    select1_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    """
    # select1_orm = models.Requests.objects.all()
    # select1_orm[0].id
    # select1_orm[0].price
    # select1_orm[0].title
    # select1_orm[0].is_success
    # todo выборка

    # todo фильтрация
    select2_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    WHERE is_success='false'
    """
    # select2_orm = models.Requests.objects.filter(is_success=False)
    # todo фильтрация

    # todo сортировка
    select3_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    ORDER BY datetime DESC
    """
    # select3_orm = models.Requests.objects.all().order_by("-datetime")
    # todo сортировка

    select_orm = models.Requests.objects.all()
    # select_orm - [<class 'django_app.models.Requests'>, ...]
    # select_orm[0] - <class 'django_app.models.Requests'>
    for i in select_orm:
        print(type(i), i)
        # i.delete()
        # i.save()
        # i.title = "Dias" + i.title
        print(i.title, i.price, i.is_success, i.description)
    # print(select_orm)
    # print(type(select_orm))

    return render(request, "django_app/requests.html", context={"select_orm": select_orm})


def get_request(request, pk):
    # id(1) - зарезервирована
    # todo выборка
    select1_raw = """
    SELECT id, title, description, price, is_success, datetime FROM Requests
    WHERE id = 1
    """
    select1_orm = models.Requests.objects.get(id=int(pk))
    print(type(select1_orm))
    print(select1_orm)
    # select1_orm.title
    # select1_orm.price
    # select1_orm.is_success
    # todo выборка

    return render(request, "django_app/request.html", context={"req": select1_orm})


def post_request(request):
    return HttpResponse("register")


def delete_requests(request):
    return HttpResponse("register")


def update_request(request):
    return HttpResponse("register")


# todo REQUESTS ###############################################


def register(request):
    return HttpResponse("register")


def recover(request):
    return HttpResponse("recover")


def recover_new(request):
    pass
