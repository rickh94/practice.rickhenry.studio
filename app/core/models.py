from django.contrib.auth import get_user_model
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    teacher = models.ForeignKey(
        "core.Teacher",
        on_delete=models.CASCADE,
    )


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
