from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404
import ipdb

class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        # ipdb.set_trace()
        album_id = self.kwargs["pk"]
        album = get_object_or_404(Album, pk=album_id)

        self.check_object_permissions(self.request, album)
        serializer.save(album=album)

    