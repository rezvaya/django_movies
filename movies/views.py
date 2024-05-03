from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    data = Movie.objects.all()
    print(data)
    return render(request, 'movie_list.html', {'movies': data})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            year = form.cleaned_data['year']
            Movie.objects.create(title=title, description=description, year=year)
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_add.html', {'form': form})

def about(request):
    return render(request, 'about.html')