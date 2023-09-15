from core.models import Student, Teacher
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Decoration(models.Model):
    name = models.CharField(max_length=100)
    svg = models.TextField()


# TODO: add highlight choices


class HighlightColor(models.TextChoices):
    RED = "text-red-600", _("Red")
    ORANGE = "text-orange-600", _("Orange")
    AMBER = "text-amber-600", _("Amber")
    YELLOW = "text-yellow-600", _("Yellow")
    LIME = "text-lime-600", _("Lime")
    GREEN = "text-green-600", _("Green")
    EMERALD = "text-emerald-600", _("Emerald")
    TEAL = "text-teal-600", _("Teal")
    CYAN = "text-cyan-600", _("Cyan")
    SKY = "text-sky-600", _("Sky")
    BLUE = "text-blue-600", _("Blue")
    INDIGO = "text-indigo-600", _("Indigo")
    VIOLET = "text-violet-600", _("Violet")
    FUCHSIA = "text-fuchsia-600", _("Fuchsia")
    PINK = "text-pink-600", _("Pink")
    ROSE = "text-rose-600", _("Rose")


class Checklist(models.Model):
    steps = models.JSONField(default=list)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="checklists"
    )
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="checklists"
    )
    decoration1 = models.ForeignKey(
        Decoration, on_delete=models.SET_NULL, related_name="+", null=True, blank=True
    )
    decoration2 = models.ForeignKey(
        Decoration, on_delete=models.SET_NULL, related_name="+", null=True, blank=True
    )
    highlight = models.CharField(
        max_length=100, choices=HighlightColor.choices, default=HighlightColor.SKY
    )
