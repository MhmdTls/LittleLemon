from django.shortcuts import render
from rest_framework import generics, viewsets  # add viewsets here
from .models import Menu, Booking             # import Booking model too
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


# Handles GET (list all) and POST (create new)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (single item), PUT, DELETE
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Booking API viewset
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


    from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

