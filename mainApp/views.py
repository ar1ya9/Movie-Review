from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.
def home(request):
    query = request.GET.get('title')
    allmovies=None
    if query:
        allmovies = Movies.objects.filter(name__icontains=query)
    else:
        allmovies = Movies.objects.all()
    context = {
        "movie": allmovies,
    }
    return render(request, 'main/index.html',context)

def details(request,id):
    movie=Movies.objects.get(id=id)
    review = MovieReview.objects.filter(movie=id).order_by('-comment')
    average = review.aggregate(Avg('rating'))
    if average == None:
        average=0
    context = {
        "movie":movie,
        "review":review,
        "average":average
    }
  
    return render(request,'main/details.html',context)

def addmovie(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form=MovieForm(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("mainApp:home")
            else:
                form = MovieForm()
            return render(request,'main/addmovie.html',{'form':form,'controller':"Add Movie"})
        else:
            return redirect('mainApp:home')
        
    return redirect('Accounts:login')

def editmovie(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
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
        else:
         return redirect('mainApp:home')
        
    return redirect('Accounts:login')

def deletemovie(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            movie=Movies.objects.get(id=id)
            movie.delete()
            return redirect('mainApp:home')
        else:
         return redirect('mainApp:home')
        
    return redirect('Accounts:login')

def adreview(request,id):
    if request.user.is_authenticated:
        movie = Movies.objects.get(id=id)
        if request.method == 'POST':
            form=ReviewForm(request.POST or None)
            if form.is_valid():
                data=form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect('mainApp:details', id)
        else:
            form = ReviewForm()
        return render(request,'main/details.html', {'form':form})
    else:
        return redirect('Accounts:login')
    
def edreview(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movies.objects.get(id=movie_id)
        review = MovieReview.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data=form.save(commit=False)
                    if (data.rating >10) or (data.rating <0):
                        error='Out of Range .Please Select 0 to 10'
                        return render(request,'main/editrev.html',{'error':error,'form':form})
                    else:
                        form.save()
                        return redirect('mainApp:details', movie_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editrev.html', {'form': form})
        else:
            return redirect('Accounts:login')
    else:
        return redirect('Accounts:login')

def dereview(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movies.objects.get(id=movie_id)
        review = MovieReview.objects.get(movie=movie, id=review_id)

        if request.user == review.user:
            review.delete()
        return redirect('mainApp:details', movie_id)
    else:
        return redirect('Accounts:login')



    