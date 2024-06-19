from django.urls import path
from mix.views import *


urlpatterns = [
    path('category/', MixCategoryAPIView.as_view(), name='category'),
    path('mix/', MixAPIView.as_view(), name='mix'),
    path('<int:pk>/', MixDetailView.as_view(), name='mix-detail'),
    path('strength/<int:pk>/', StrengthAPIView.as_view(), name='strength'),
]
