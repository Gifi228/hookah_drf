from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from mix.models import *
from mix.serializer import *


class MixCategoryAPIView(ListAPIView):
    queryset = MixCategory.objects.all()
    serializer_class = MixCategorySerializer


class MixAPIView(ListAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer


class StrengthAPIView(RetrieveAPIView):
    queryset = Strength.objects.all()
    serializer_class = StrengthSerializer


class MixDetailView(RetrieveAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixDetailSerializer
