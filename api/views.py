# api/views.py

from rest_framework import generics
from .serializers import PersonSerializer
from .models import Person

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Person."""
        serializer.save()

# api/views.py

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Person.objects.all()
    serializer_class = PersonSerializer