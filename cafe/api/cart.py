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
            cart=cart,
            course=course
        ).save()
    return cart_item


def empty_cart(session: Session):
    try:
        cart = Cart.objects.get(session=session).delete()
        return True
    except:
        return False


def remove_from_cart(cart_item_id: int):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id).delete()
        return True
    except:
        return False


def make_cart_payment(session: Session):
    try:
        cart = Cart.objects.get(session=Session, is_paid=False)
    except:
        return False
    cart.is_paid = None
    cart.save()
    return cart
