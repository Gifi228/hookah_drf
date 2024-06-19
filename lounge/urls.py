from django.urls import path
from lounge.views import *

urlpatterns = [
    path('lounge-images/', LoungeImagesView.as_view(), name='lounge-images' ),
    path('lounge/', LoungeAPIView.as_view(), name='lounge'),
    path('lounge-detail/<int:pk>/', LoungeDetailView.as_view(), name='lounge-detail')
]
