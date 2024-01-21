from django.shortcuts import render


def main_view(request):

    context = {}

    return render(request, "mainpage/home.html", context)


def unauthorized_access(request):

    context = {}

    return render(request, "mainpage/unauthorized.html", context)
