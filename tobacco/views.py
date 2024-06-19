from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from tobacco.models import *
from tobacco.serializer import *


class TobaccoListView(ListAPIView):
    queryset = Tobacco.objects.all()
    serializer_class = TobaccoListSerializer


class TobaccoDetailView(RetrieveAPIView):
    queryset = Tobacco.objects.all()
    serializer_class = TobaccoDetailSerializer


class TobaccoImagesView(ListAPIView):
    queryset = TobaccoImages.objects.all()
    serializer_class = TobaccoImagesSerializer





