from django.shortcuts import render

from .models import blogModel

def index(request):
    return render(request, 'blogApp/index.html')

def userIndex(request):
    form_list = blogModel.objects.filter(username=request.user)
    context = {'form_list': form_list}
    return render(request, 'blogApp/profile.html', context)

def newsFeed(request):
    form_list = blogModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'blogApp/newsFeed.html', context)