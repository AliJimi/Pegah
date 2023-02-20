from django.urls import path

from cafe.views.main import landing_view, main_view
from cafe.views.menu import menu_view, menu_courses_api, add_course, CourseCreateView
from cafe.views.reservation import reservation_view, reservation_today_view, reservation_today_api


app_name = "cafe"

urlpatterns = [
    path('', main_view,),
    path('menu/', menu_view, name='menu'),
    path('menu/courses/api/', menu_courses_api, name='menu-courses-api'),

    path('menu/courses/', menu_courses_api, name='menu-courses'),
    path('menu/courses/add/', add_course, name='menu-courses-add'),
    path('landing/', landing_view, name='landing'),

    path('reservation/', reservation_view, name='reservation'),

    path('reservation/today/', reservation_today_view, name='reservation-today'),
    path('reservation/today/api/', reservation_today_api, name='reservation-today-api'),

    path('a/add/', CourseCreateView.as_view(), name='reservation2'),
]
