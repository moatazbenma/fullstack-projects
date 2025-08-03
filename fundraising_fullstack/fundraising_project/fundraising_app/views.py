from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def intern_api(request):
    data = {
        "name": "El Mouataz Benmanssour",
        "referral_code": "ELMOUATAZ2025",
        "amount_raised": 1200
    }
    return JsonResponse(data)



def dashboard(request):
    data={
        "name":"El Mouataz Benmanssour",
        "referral_code": "ELMOUATAZ2025",
        'total_donations': 1200
    }
    return render(request, 'fundraising_app/dashboard.html', {"intern_data": data})

def leaderboard(request):
    leaderboard_data = [
        {"name": "Hassan", "referral_code": "HASSAN2025", "amount": 2200},
        {"name": "Khalid", "referral_code": "KHALID2025", "amount": 1800},
        {"name": "El Mouataz Benmanssour", "referral_code": "ELMOUATAZ2025", "amount": 1200},
    ]
    return render(request, 'fundraising_app/leaderboard.html', {"leaders": leaderboard_data})



def login_page(request):
    return render(request, 'fundraising_app/login.html')


def signup_view(request):
    return render(request, 'fundraising_app/signup.html')
