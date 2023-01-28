from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from Pegah.messages import cafe_messages
from cafe.models.course import get_available_courses, get_courses, get_course_class, add_course_row


def menu_view(request):
    return render(request, 'cafe/menu.html',)


def menu_courses_api(request):
    courses = get_available_courses()
    return JsonResponse(courses, safe=False)


@login_required(login_url='/login/')
def add_course(request):
    courses_dict = get_courses()
    if request.method == "POST":
        try:
            image = request.FILES.get('image', None)
            name = request.POST.get('name', None)
            course = get_course_class(request.POST.get('course', None))
            description = request.POST.get('description', None)
            price = request.POST.get('price', None)
            if name and course and price:
                add_course_row(course, name, description, price, image)
        except:
            return HttpResponse("Fail", status=400)
        return HttpResponse(cafe_messages['add-course-success']['fa'])

    return render(request, 'cafe/admin/add-course.html', {
        'courses': [course['name'] for _, course in courses_dict.items()],
    })

