from django.contrib.sessions.models import Session
from django.db import models

from cafe.models.course import Course


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def to_json(self):
        pass


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_count = models.PositiveSmallIntegerField(null=False, blank=False, default=1, max_length=3)

    def add_to_course_count(self):
        self.course_count += 1
        self.save()

    def to_json(self):
        return {
            'course_count': self.course_count,
            'name': self.course.name,
            'price': self.course.price,
            'total_price': self.course.price * self.course_count,
            'image_url': self.course.image.url

        }
