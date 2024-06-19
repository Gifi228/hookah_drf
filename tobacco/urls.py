from django.urls import path
from tobacco.views import *


urlpatterns = [
    path('tobacco-images/', TobaccoImagesView.as_view(), name='tobacco-images'),
    path('tobacco/', TobaccoListView.as_view(), name='tobacco'),
    path('tobacco-detail/<int:pk>/', TobaccoDetailView.as_view(), name='tobacco-detail'),

]
