from django.db import models


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
