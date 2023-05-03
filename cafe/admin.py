from django.contrib import admin
from cafe.models.course import Material, Course, ColdDrink, Coffee, Milkshake, HotDrink, Dessert, Breakfast, \
    MainCourse, Appetizer, Tea, Smoothie, Salad
from cafe.models.payment import Payment, PaymentReserve, PaymentCourse
from cafe.models.reservation import Reserve
from cafe.models.table import Table
from cafe.models.cart import Cart, CartItem


admin.site.register(Material)

admin.site.register(Course)
admin.site.register(ColdDrink)
admin.site.register(Coffee)
admin.site.register(Milkshake)
admin.site.register(HotDrink)
admin.site.register(Dessert)
admin.site.register(Breakfast)
admin.site.register(MainCourse)
admin.site.register(Appetizer)
admin.site.register(Tea)
admin.site.register(Smoothie)
admin.site.register(Salad)
admin.site.register(Payment)
admin.site.register(PaymentReserve)
admin.site.register(Reserve)
admin.site.register(Table)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(PaymentCourse)
