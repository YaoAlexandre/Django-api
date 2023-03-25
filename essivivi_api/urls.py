from django.urls import path
from .views import *



urlpatterns = [
   path('categories/', ListCategories.as_view(), name= 'categories'),
   path('categories/<int:pk>/', DetailCategories.as_view(), name= 'categoriesById'),

   path('eaux/', ListEau.as_view(), name= 'eaux'),
   path('eaux/<int:pk>/', DetailEau.as_view(), name= 'eauxById'),

   path('users/', ListUser.as_view(), name= 'users'),
   path('users/<int:pk>/', DetailUser.as_view(), name= 'usersById'),


   path("agents/", AgentList.as_view(), name="allagents"),
   path('agents/<int:pk>/', AgentDetail.as_view(), name= 'agentsById'),


   path("clients/", ListClient.as_view(), name="allclients"),
   path('clients/<int:pk>/', DetailClient.as_view(), name= 'clientsById'),


   path("livraisons/", ListLivraison.as_view(), name="allLivraisons"),
   path('livraisons/<int:pk>/', DetailLivraison.as_view(), name= 'LivraisonsById'),


]