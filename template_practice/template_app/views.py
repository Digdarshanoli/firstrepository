from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "template_practice/index.html")


def about(request):
    return render(request, "template_practice/about.html")

def help(request):
    return render(request, "template_practice/help.html")