from django.shortcuts import render, redirect

# Create your views here.


def gallery(request):
    return render(request, 'gallery.html')
