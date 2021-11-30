from django.urls import path,include
from apis import views

urlpatterns = [
   path('getHotels',views.getHotels)
]