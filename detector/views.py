from django.shortcuts import render
from .model import check_news


def home(request):
    result = ""

    if request.method == "POST":
        news = request.POST.get("news")

        if news:
            result = check_news(news)

    return render(request, "detector/home.html", {"result": result})