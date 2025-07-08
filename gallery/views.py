from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt


# Call the API and show the gallery
def gallery_view(request):
    response = requests.get("http://127.0.0.1:8000/api/photos/")
    photos = response.json()  # Get all photos as JSON
    return render(request, "gallery.html", {"photos": photos})


@csrf_exempt
def like_photo(request, photo_id):
    requests.post(f"http://127.0.0.1:8000/api/photos/{photo_id}/like/")
    return redirect("/")


@csrf_exempt
def dislike_photo(request, photo_id):
    requests.post(f"http://127.0.0.1:8000/api/photos/{photo_id}/dislike/")
    return redirect("/")
