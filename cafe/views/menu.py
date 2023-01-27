from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from cafe.models.course import get_available_courses, get_courses


def menu_view(request):
    return render(request, 'cafe/menu.html',)


def menu_courses_api(request):
    courses = get_available_courses()
    return JsonResponse(courses, safe=False)


@login_required(login_url='/login/')
def add_course(request):
    courses_dict = get_courses()
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print(request.POST.get('image'))

    return render(request, 'cafe/admin/add-course.html', {
        'courses': [course['name'] for _, course in courses_dict.items()],
    })

