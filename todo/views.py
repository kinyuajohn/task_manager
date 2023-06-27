from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here.
def home(request):
    client_list = [
        {
            "id": "1",
            "name": "John Smith",
            "profession": "Web Developer",
        },
        {
            "id": "2",
            "name": "Luke Warren",
            "profession": "Accountant",
        },
    ]

    context = {
        "client_list": client_list,
    }

    return render(request, "index.html", context=context)


def register(request):
    return render(request, "register.html")


def my_login(request):
    return render(request, "my-login.html")
