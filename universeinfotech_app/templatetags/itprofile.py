from django import template
from universeinfotech_app.models import IT_Profile

register = template.Library()

@register.filter
def itprofile(request):
    return IT_Profile.objects.all().order_by('-id')[:1]
