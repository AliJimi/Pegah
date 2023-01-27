from django.shortcuts import render


def main_view(request):
    return render(request, 'cafe/landing.html')


def landing_view(request):
    return render(request, 'cafe/landing.html')
