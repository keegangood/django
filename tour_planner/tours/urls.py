from django.urls import path

from . import views

app_name="tours"
urlpatterns = [
    path('', views.TourLegView.as_view(), name="home"),
    path('tours/', views.tours, name="tours"),
    path('edit/<int:tourleg_id>', views.edit, name="edit")
]