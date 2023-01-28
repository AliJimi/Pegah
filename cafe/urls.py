from django.urls import path

from cafe.views.main import landing_view, main_view
from cafe.views.menu import menu_view, menu_courses_api, add_course
from cafe.views.reservation import reservation_view

urlpatterns = [
    path('', main_view,),
    path('menu/', menu_view, name='cafe-menu'),
    path('menu/courses/api/', menu_courses_api, name='cafe-menu-courses-api'),

    path('menu/courses/', menu_courses_api, name='cafe-menu-courses'),
    path('menu/courses/add/', add_course, name='cafe-menu-courses-add'),
    path('landing/', landing_view, name='cafe-landing'),

    path('reservation/', reservation_view, name='cafe-reservation'),
]
