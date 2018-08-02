from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(request):
    events = Entry.objects.all()
    return render(request, 'myapp/index.html', {'events':events})

def detail(request,pk):
    detail = Entry.objects.get(pk=pk)
    
    return render(request, 'myapp/detail.html',{'detail':detail})
