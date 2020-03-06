from django.shortcuts import render

from django.views.generic import TemplateView
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
        else:
            return render(request, self.template_name,  {'form':form})
        
        return render(request, self.template_name,  {'form':form})


'''
# Create your views here.
class AddMovieView(TemplateView):
    template_name = 'movies/add.html'

    def get(self, request):
        form = MovieAddForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        # create the form instance but with data from the post
        form = MovieAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            year = form.cleaned_data['year']

            new_movie = Movie(title=title, director=director, year=year)
            new_movie.save()
        
        return render(request, self.template_name,  {'form':form})
'''