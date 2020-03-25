from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from .forms import MovieAddForm
from .models import Movie

# Create your views here.
class MovieAddView(TemplateView):
    template_name = 'movies/add.html'

    def get(self, request):
        form = MovieAddForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = MovieAddForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            director = form.cleaned_data['director']
            synopsis = form.cleaned_data['synopsis']

            new_movie = Movie(title=title, year=year, director=director, synopsis=synopsis)
            new_movie.save()
            return HttpResponseRedirect(reverse('movies-list'))
        else:
            return render(request, self.template_name,  {'form':form})
        
        return render(request, self.template_name,  {'form':form})

class MovieDetailView(TemplateView):
    template_name = 'movies/detail.html'
    id = None

    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        return render(request, self.template_name, {'movie':movie})

class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'


class MovieUpdateView(TemplateView):
    template_name = 'movies/movie_update.html'
    id = None

    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        if movie:
            form = MovieAddForm(initial={'title':movie.title, 'year':movie.year, 'director':movie.director, 'synopsis':movie.synopsis})
            print(form)
            return render(request, self.template_name, {'form':form})
    
    def post(self, request, id):
        form = MovieAddForm(request.POST)
        movie = Movie.objects.get(id=id)
        if form.is_valid():
            movie.title = form.cleaned_data['title']
            movie.year = form.cleaned_data['year']
            movie.director = form.cleaned_data['director']
            movie.synopsis = form.cleaned_data['synopsis']

            movie.save()
            return HttpResponseRedirect(reverse('movies-list'))


            