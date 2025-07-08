from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Photo
from .serializers import PhotoSerializer


# ViewSet gives list, create, retrieve, update, delete
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    # Add custom like endpoint
    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        photo = self.get_object()
        photo.likes += 1
        photo.save()
        return Response({"status": "photo liked", "likes": photo.likes})

    # Add custom dislike endpoint
    @action(detail=True, methods=["post"])
    def dislike(self, request, pk=None):
        photo = self.get_object()
        photo.dislikes += 1
        photo.save()
        return Response({"status": "photo disliked", "dislikes": photo.dislikes})
