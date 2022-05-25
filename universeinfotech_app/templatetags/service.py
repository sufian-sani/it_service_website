from django import template
from universeinfotech_app.models import Our_Service

register = template.Library()

@register.filter
def service(request):
    return Our_Service.objects.all()[:6]
