from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(request):
    events = Entry.objects.all()
    return render(request, 'myapp/index.html', {'events':events})
