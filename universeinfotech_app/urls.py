from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='home'),
    path('developer_team/', developer_team , name='developer_team'),
    path('blog/', blog , name='blog'),
    path('about/', about , name='about'),
    path('service/', service , name='service'),
    path('feature/', feature , name='feature'),
    path('portfolio/', portfolio , name='portfolio'),
    path('history/', history , name='history'),
    path('client/', client , name='client'),
    path('contact/', contact , name='contact'),
    path('career/', career , name='career'),
    path('news_and_evenet/', news_and_evenet, name='news-and-evenet'),
    path('notice/', notice, name='notice'),
    path('mission_and_vission/', mission_and_vission, name='mission-and-vission'),
    #delails page path
    path('feature/<slug>', FeatureDetails, name='feature-detail'),
    path('service/<slug>', ServiceDetails, name='service-detail'),
    path('blog/<slug>', BlogDetails, name='blog-detail'),
    path('career/details/<slug>', careerdetails , name='career-detail'),

]