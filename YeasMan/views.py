from django.shortcuts import render

# Create your views here.
def index(request):
    info = {
        "helloText": "Hello world"
    }
    return render(request, "Hello.html", context=info)