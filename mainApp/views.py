from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allmovies = Movies.objects.all()
    context = {
        "movie": allmovies,
    }
    return render(request, 'main/index.html',context)

def details(request,id):
    movie=Movies.objects.get(id=id)
    context ={
        "movie":movie
    }
    return render(request,'main/details.html',context)

def addmovie(request):
    if request.method == 'POST':
        form=MovieForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("mainApp:home")
    else:
        form = MovieForm()
    return render(request,'main/addmovie.html',{'form':form,'controller':"Add Movie"})

def editmovie(request,id):
    movie=Movies.objects.get(id=id)
    if request.method == 'POST':
        form=MovieForm(request.POST or None,instance=movie)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('mainApp:details', id=id)

    else:
        form = MovieForm(instance=movie)

    return render(request,'main/addmovie.html',{'form':form,'controller':"Edit Movie"})

def deletemovie(request,id):
    movie=Movies.objects.get(id=id)
    movie.delete()
    return redirect('mainApp:home')

    