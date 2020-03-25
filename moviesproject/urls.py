"""moviesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from moviesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/add/', views.MovieAddView.as_view(), name='movies-add'),
    path('movies/all/', views.MoviesListView.as_view(), name='movies-list'),
    path('movies/update/<int:id>', views.MovieUpdateView.as_view(), name='movies-update'),
    path('movies/detail/<int:id>', views.MovieDetailView.as_view(), name="movies-detail"),
]
