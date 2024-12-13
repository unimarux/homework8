from django import template
from ..models import Type , Flower

register = template.Library()


@register.simple_tag
def get_categories():
    return Type.objects.all()