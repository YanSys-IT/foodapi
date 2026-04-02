from django.db import models
from model_utils.models import TimeStampedModel


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, unique=True, blank=True, null=True)
    name_ch = models.CharField(max_length=255, unique=True, blank=True, null=True)
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        ordering = ('order_id',)


class Food(TimeStampedModel):
    category = models.ForeignKey(FoodCategory, related_name='food', on_delete=models.CASCADE)
    is_vegan = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    code = models.IntegerField()
    internal_code = models.IntegerField(unique=True, null=True, blank=True)
    name_ru = models.CharField(max_length=255)
    description_ru = models.CharField(max_length=255, blank=True, null=True)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    description_ch = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_publish = models.BooleanField(default=True)
    additional = models.ManyToManyField('self', symmetrical=False, related_name='additional_from', blank=True)

    def __str__(self):
        return self.name_ru
