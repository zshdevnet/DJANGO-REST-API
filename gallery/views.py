from django.shortcuts import render, redirect
import requests
from django.views.decorators.csrf import csrf_exempt
import os


# Call the API and show the gallery
def gallery_view(request):

    BASE_API_URL = os.getenv("API_BASE_URL")  # FALLBACK OR LOCAL

    try:
        response = requests.get(f"{BASE_API_URL}/api/photos/")
        photos = response.json()  # Get all photos as JSON
        return render(request, "gallery.html", {"photos": photos})
    except Exception as e:
        photos = []
        print("API error: ", e)
        return render(request, "gallery.html", {"photos": photos})


@csrf_exempt
def like_photo(request, photo_id):
    BASE_API_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
    try:
        requests.post(f"{BASE_API_URL}/api/photos/{photo_id}/like/")
    except Exception as e:
        print("Like API error: ", e)
    return redirect("/")


@csrf_exempt
def dislike_photo(request, photo_id):
    BASE_API_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
    try:
        requests.post(f"{BASE_API_URL}/api/photos/{photo_id}/dislike/")
    except Exception as e:
        print("Dislike API error: ", e)
    return redirect("/")
