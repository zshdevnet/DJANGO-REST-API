from django.urls import path
from . import views

urlpatterns = [
    path("", views.gallery_view, name="gallery"),
    path("like/<int:photo_id>/", views.like_photo, name="like_photo"),
    path("dislike/<int:photo_id>/", views.dislike_photo, name="dislike_photo"),
]
