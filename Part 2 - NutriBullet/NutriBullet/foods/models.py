from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Food(models.Model):
    class FoodType(models.TextChoices):
        MEAT = 'MEAT', _("Meat")
        FRUIT = 'FRUIT', _("Fruit")
        VEGETABLE = 'VEGETABLE', _("Vegetable")
        GRAINS = 'GRAINS', _("Grains")
        DAIRY = 'DAIRY', _("Dairy")
        NUTS = 'NUTS', _("Nuts")
        SUGAR = 'SUGAR', _("Sugar")
        BEVERAGES = 'BEVERAGES', _("Beverages")
    name = models.CharField(max_length=20)
    food_type = models.SlugField(choices=FoodType.choices, default=FoodType.MEAT)
    kcal = models.FloatField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    carbohydrates = models.FloatField()
    sugars = models.FloatField()
    protein = models.FloatField() 
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name