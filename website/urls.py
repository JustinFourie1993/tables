from . import views
from django.urls import path


urlpatterns = [
    path('menu/', views.MealList.as_view(), name='menu'),
    path('', views.index, name='home'),
    path('booking/', views.make_booking, name='booking'),
    path('booking/edit/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
]