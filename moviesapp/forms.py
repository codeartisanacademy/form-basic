from django import forms

from .models import Movie

class MovieAddForm(forms.Form):
    title = forms.CharField(max_length=200)
    year = forms.IntegerField()
    director = forms.CharField(max_length=200)
    synopsis = forms.CharField(widget=forms.TextInput())


'''
class MovieAddForm(forms.Form):
    title = forms.CharField(max_length=200, label='Judul')
    year = forms.IntegerField()
    director = forms.CharField(max_length=200)

    def clean_title(self):
        title = self.cleaned_data['title']
        movie = Movie.objects.get(title=title)
        if movie:
            raise forms.ValidationError('The movie exists in database')

        return movie
'''