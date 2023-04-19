from django.contrib.sessions.models import Session
from cafe.models.cart import Cart, CartItem
from cafe.models.course import Course


def add_to_cart(session: Session, course_id):
    try:
        cart = Cart.objects.get(session=session)
    except:
        cart = Cart(
            session=session
        ).save()
    try:
        course = Course.objects.get(id=course_id, is_available=True)
    except:
        return False

    try:
        cart_item = CartItem.objects.get(cart=cart, course=course)
        cart_item.add_to_course_count()
    except:
        cart_item = CartItem(
            session=session,
            course=course
        ).save()
    return cart_item.to_json()


def empty_cart():
    pass


def remove_from_cart():
    pass
