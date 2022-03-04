from django.db import models
import datetime
# from django.utils.translation import gettext as _

today = datetime.date.today()


class PicturesMedicine(models.Model):
    image = models.ImageField(upload_to=f'medicine_pictures/{today.year}-{today.month}-{today.month}/',
                              null=True, blank=True)


class TypeMedicine(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=f'types/', null=True, blank=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    image = models.ImageField(upload_to=f'medicine/', null=True, blank=True)
    pictures = models.ManyToManyField(PicturesMedicine, blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    order_count = models.IntegerField(default=0)
    description = models.TextField(null=True)
    quantity = models.IntegerField(default=0)
    review = models.IntegerField(default=0)
    type_medicine = models.ForeignKey(TypeMedicine, on_delete=models.RESTRICT, null=True)
    cost = models.IntegerField(null=True)
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
