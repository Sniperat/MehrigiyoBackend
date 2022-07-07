from django.db import models

from account.models import UserModel
from shop.models import Medicine
from specialist.models import Doctor


class CommentMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.RESTRICT)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    text = models.TextField()
    rate = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True, null=True)


class CommentDoctor(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name='comments_doc')
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    text = models.TextField(null=True, blank=True)
    rate = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True, null=True)

