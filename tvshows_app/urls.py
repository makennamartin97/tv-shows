from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('create', views.create),
    path('shows/<int:showID>', views.showinfo),
    path('shows/<int:showID>/edit', views.edit),
    path('shows/<int:showID>/update', views.update),
    path('shows/<int:showID>/destroy', views.destroy),
]