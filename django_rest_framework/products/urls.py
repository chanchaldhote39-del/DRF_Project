from django.urls import path
from .import views 

urlpatterns = [
    path('products/', views.Product_list.as_view()),
    path('products/<int:pk>/', views.ProductDetialView.as_view()),
     

]