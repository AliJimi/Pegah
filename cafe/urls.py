from django.urls import path

from cafe.views.main import landing_view, main_view
from cafe.views.menu import menu_view

urlpatterns = [
    path('', main_view,),
    path('menu/', menu_view, name='cafe-menu'),
    path('landing/', landing_view, name='cafe-landing'),
]