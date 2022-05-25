from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def index(request):
    features = Feature.objects.all()
    banner_sliders = Banner_Slider.objects.all()
    services_part_1 = Our_Service.objects.all()[:2]
    services = Our_Service.objects.all()[2:6]
    project_gallery = Project_Gallery.objects.all()
    clientsreview =ClientsReview.objects.all()
    tools = Tools.objects.all()

    context={
        'banner_sliders':banner_sliders,
        'features':features,
        'services':services,
        'services_part_1':services_part_1,
        'project_gallery':project_gallery,
        'clientsreview':clientsreview,
        'tools':tools
    }
    return render(request, 'index.html',context)

def feature(request):
    features = Feature.objects.all()
    context={
        'features':features
    }
    return render(request, 'feature.html', context)

def FeatureDetails(request,slug):
    features = Feature.objects.get(slug=slug)

    context={
        'features':features,
    }
    return render(request, 'featuredetail.html',context)
    
def service(request):
    services = Our_Service.objects.all()
    context={
        'services':services
    }
    return render(request, 'service.html', context)

def ServiceDetails(request,slug):
    services = Our_Service.objects.get(slug=slug)

    context={
        'services':services,
    }
    return render(request, 'servicesdetail.html',context)

def blog(request):
    blogs = Blog.objects.all()

    context ={
        'blogs':blogs
    }
    return render(request, 'blog.html',context)

def BlogDetails(request,slug):
    blogs = Blog.objects.get(slug=slug)
    more_blog = Blog.objects.all().exclude(slug=slug)

    context={
        'blogs':blogs,
        'more_blog':more_blog
    }
    return render(request, 'blogdetail.html',context)


def developer_team(request):
    developer_profile = Developer_Profile.objects.all()

    context={
        'developer_profile':developer_profile
    }
    return render(request, 'developer_team.html',context)

def client(request):
    clients = Our_Client.objects.all()

    context={
        'clients':clients
    }
    return render(request, 'clients.html',context)

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()

    context={
        'portfolios':portfolios
    }
    return render(request, 'portfolio.html', context)

def history(request):
    return render(request, 'history.html')

def contact(request):
    return render(request, 'contact.html')


def career(request):
    careers = Career.objects.filter(active_status=True)

    context={
        'careers':careers
    }
    return render(request, 'career.html',context)

def careerdetails(request,slug):
    careers =Career.objects.get(slug=slug)
    form =JobApplicationForm()
    if request.method == 'POST':
        form =JobApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submit Your Application')
            return redirect('career-detail', slug=slug)
    context={
        'careers':careers,
        'form':form
    }
    return render(request, 'careerdetails.html',context)

def news_and_evenet(request):
    news_and_evenets = News_and_Evenet.objects.last()

    context={
        'news_and_evenets':news_and_evenets,
    }

    return render(request, 'news_and_evenet.html', context)

def notice(request):
    notice = Notice.objects.last()

    context={
        'notice':notice,
    }

    return render(request, 'notice.html', context)

def mission_and_vission(request):
    mission = MissionVission.objects.filter(object_type='mission').last()
    vission = MissionVission.objects.filter(object_type='vission').last()
    context={
        'mission':mission,
        'vission':vission,
    }

    return render(request, 'mission_and_vission.html', context)

def it_profile(request):
    notice = IT_Profile.objects.last()

    context={
        'notice':notice,
    }

    return render(request, 'notice.html', context)
