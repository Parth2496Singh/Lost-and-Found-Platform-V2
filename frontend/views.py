from django.shortcuts import render, redirect
import requests

# Create your views here.

BASE_API_URL = "http://127.0.0.1:8000/api"

def index(request):
    print("INDEX VIEW CALLED")
    return render(request, 'home.html')

# Temporary placeholders for other pages
def report_lost(request):
    print("REPORT LOST VIEW CALLED")
    return render(request, 'report_lost.html')

def report_found(request):
    return render(request, 'report_found.html')

def search(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def lost_detail(request, id):
    try:
        response = requests.get(f"{BASE_API_URL}/lost-items/{id}/")
        response.raise_for_status()
        item = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching lost item:", e)
        item = None

    return render(request, "lost_detail.html", {"item": item , "id": id})

def found_detail(request, id):
    try:
        response = requests.get(f"{BASE_API_URL}/found-items/{id}/")
        response.raise_for_status()
        item = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching found item:", e)
        item = None

    return render(request, "found_detail.html", {"item": item, "id": id})


def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_of_service(request):
    return render(request, "terms_of_service.html")

def signup_page(request):
    return render(request, 'sign_up.html')

def login_view(request):
    """
    Serve the login page.
    Optionally pass 'next' parameter if redirected from another page.
    """
    next_url = request.GET.get('next', '')  # capture 'next' from URL
    return render(request, "login.html", {"next": next_url})

def my_reports(request):
    """
    Render the 'My Reports' page for logged-in users.
    """
    if not request.user.is_authenticated:
        # Redirect to login if not logged in
        return redirect(f"/login/?next=/my-reports/")

    return render(request, "my_reports.html")