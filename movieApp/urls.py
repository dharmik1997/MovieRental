#first commit
# adding feature 1

from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.all_customers),
    path('available-movies/<int:cust_id>', views.available_movies),
    path('rent-movie/<int:cid>/<int:mid>', views.rent_movie),
    path('get-all/', views.all_customers),
    path('customers/add_user/', views.add_user),
    path('customers/get-detail/<int:cid>/', views.get_detail),
    path('customers/get-detail/<int:cid>/unrent/', views.unrent)
]
