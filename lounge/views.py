from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from lounge.models import *
from lounge.serializer import *


class LoungeImagesView(ListAPIView):
    queryset = LoungeImages.objects.all()
    serializer_class = LoungeImagesSerializer


class LoungeAPIView(ListAPIView):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer


class LoungeDetailView(RetrieveAPIView):
    queryset = Lounge.objects.all()
    serializer_class = LoungeDetailSerializer
