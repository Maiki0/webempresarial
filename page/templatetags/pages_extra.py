'''from django import template
from page.models import Page

register = template.library()

@register.simple_tag
def get_pages():
    pages = Page.objects.all()
    return pages'''