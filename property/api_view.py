from .models import Property
from .serailizers import PropertySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PropertyApiList(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]


class PropertyApiDetail(RetrieveUpdateDestroyAPIView):
     queryset = Property.objects.all()
     serializer_class = PropertySerializer
     permission_classes = [IsAuthenticated]
