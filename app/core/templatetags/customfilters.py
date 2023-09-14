from django import template
from django.contrib import messages
from django.forms import BoundField
from django.utils.safestring import SafeString

register = template.Library()


@register.filter(name="addclass")
def addclass(value: BoundField, arg: str) -> SafeString:
    return value.as_widget(attrs={"class": arg})


@register.filter(name="icon_from_word")
def icon_from_word(value: str) -> str | None:
    if c := value[0]:
        return c.upper()
    return None


@register.filter(name="message_color")
def message_color(level: int) -> str:
    if level == messages.DEBUG or level == messages.ERROR:
        return "bg-bittersweet-400"
    elif level == messages.SUCCESS:
        return "bg-green-100"
    elif level == messages.INFO:
        return "bg-pictonblue-400"
    return "bg-midaro-200"
