from django import template
from django.template import engines
from django.template.context import Context
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def render_template(value):
    print(engines['django'].from_string(value).render(Context()))
    return engines['django'].from_string(value).render(Context())
