from django.db import models
from django.forms import ModelForm


class Material(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # materials = models.ManyToManyField(Material)
    count = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    price = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='food/')

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'is_available': self.is_available,
            'price': self.price,
            'image_url': self.image.url,
        }

    def __str__(self):
        return f'Course {self.name}'


class ColdDrink(Course):
    pass


class Coffee(Course):
    pass


class Milkshake(Course):
    pass


class HotDrink(Course):
    pass


class Dessert(Course):
    pass


class Breakfast(Course):
    pass


class MainCourse(Course):
    pass


class Appetizer(Course):
    pass


class Tea(Course):
    pass


class Smoothie(Course):
    pass


class Salad(Course):
    pass


def get_available_courses():
    return {
        "cold_drinks": [course.to_json() for course in ColdDrink.objects.filter(is_available=True)],
        "coffees": [course.to_json() for course in Coffee.objects.filter(is_available=True)],
        "milkshakes": [course.to_json() for course in Milkshake.objects.filter(is_available=True)],
        "hot_drinks": [course.to_json() for course in HotDrink.objects.filter(is_available=True)],
        "desserts": [course.to_json() for course in Dessert.objects.filter(is_available=True)],
        "breakfasts": [course.to_json() for course in Breakfast.objects.filter(is_available=True)],
        "main_courses": [course.to_json() for course in MainCourse.objects.filter(is_available=True)],
        "appetizers": [course.to_json() for course in Appetizer.objects.filter(is_available=True)],
        "teas": [course.to_json() for course in Tea.objects.filter(is_available=True)],
        "smoothies": [course.to_json() for course in Smoothie.objects.filter(is_available=True)],
        "salads": [course.to_json() for course in Salad.objects.filter(is_available=True)],
    }


def get_courses():
    return {
        "cold_drink": {'name': '?????????????? ??????', 'class': ColdDrink},
        "coffee": {'name': '????????', 'class': Coffee},
        "milkshake": {'name': '??????', 'class': Milkshake},
        "hot_drink": {'name': '?????????????? ??????', 'class': HotDrink},
        "dessert": {'name': '??????', 'class': Dessert},
        "breakfast": {'name': '????????????', 'class': Breakfast},
        "main_course": {'name': '???????? ????????', 'class': MainCourse},
        "appetizer": {'name': '???????????????', 'class': Appetizer},
        "tea": {'name': '??????', 'class': Tea},
        "smoothie": {'name': '????????????', 'class': Smoothie},
        "salad": {'name': '??????????', 'class': Salad},
    }


def get_course_class(course: str):
    for c, v in get_courses().items():
        if v['name'] == course:
            return v['class']
    return None


def add_course_row(course, name, description, price, image):
    course_obj = course(
        name=name, image=image, description=description, price=price
    )
    course_obj.save()
