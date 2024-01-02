from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.firstapp,name="firstapp"),
    path('data',views.data,name="firstapp"),
    path('display',views.data,name="firstapp"),

]