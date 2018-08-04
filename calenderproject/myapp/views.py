from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entry
from .forms import EntryForm

def index(request):
    events = Entry.objects.all()
    return render(request, 'myapp/index.html', {'events':events})
    #return render(request, 'myapp/demo.html')

def detail(request,pk):
    detail = Entry.objects.get(pk=pk)

    return render(request, 'myapp/detail.html',{'detail':detail})

def add(request):
    if request.method=="POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name = name,
                date = date,
                description = description,
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()

    return render(request, 'myapp/form.html',{'form':form})
