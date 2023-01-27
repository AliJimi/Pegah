from django.http import JsonResponse
from django.shortcuts import render

from cafe.models.course import Course, Coffee


def menu_view(request):
    coffees = Coffee.objects.filter(is_available=True)

    return render(request, 'cafe/menu.html', {
        'coffees': coffees,
    })


def courses_api(request):
    courses = Course.objects.filter(is_available=True)

    return JsonResponse([course.to_json() for course in courses], safe=False)
