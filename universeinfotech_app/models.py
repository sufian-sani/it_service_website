from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
class Banner_Slider(models.Model):
    title = models.CharField(max_length = 150) 
    image = models.ImageField(upload_to='Banner_slider', default='no.jpg')
    description  = models.TextField()

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    font_icon_code = models.CharField(max_length = 150) 
    description  = models.TextField()

    def __str__(self):
        return self.title

class Our_Service(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    font_icon_code = models.CharField(max_length = 150)  
    description  = models.TextField()

    def __str__(self):
        return self.title

class Project_Gallery(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    project_type = models.CharField(max_length = 50) 
    image = models.ImageField(upload_to='Project_Gallery', default='no.jpg')
    description  = models.TextField()

    def __str__(self):
        return self.title

class Developer_Profile(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    designation = models.CharField(max_length = 50) 
    image = models.ImageField(upload_to='Developer_Profile', default='no.jpg')
    facebook_link = models.URLField(max_length = 200, blank=True, null=True)
    twitter_link = models.URLField(max_length = 200, blank=True, null=True)
    dribbble_link = models.URLField(max_length = 200, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='BlogImage', default='no.jpg')
    description =RichTextUploadingField('descriptions')
    
    def __str__(self):
        return self.title

class Our_Client(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ClientsImg')
    
    def __str__(self):
        return self.name

class ClientsReview(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ClientsImg')
    review  = models.CharField(max_length = 250)
    rating  = models.FloatField()

    def __str__(self):
        return self.name

class Tools(models.Model):
    tilte = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ToolsImg')
    
    def __str__(self):
        return self.tilte
    

class Portfolio(models.Model):
    tilte = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ToolsImg')
    portfolio_link = models.URLField(max_length = 200)
    
    
    def __str__(self):
        return self.tilte

class Career(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    active_status = models.BooleanField(default=True)
    job_description =RichTextUploadingField()
    job_requirement =RichTextUploadingField()
    educational_eequirements =RichTextUploadingField()
    compensation_other_benefits =RichTextUploadingField()
    experience = models.CharField(max_length = 150) 
    salary = models.CharField(max_length = 150)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title    
    
    
class JobApplication(models.Model):
    full_name= models.CharField(max_length = 150)
    email = models.EmailField()
    phone= models.CharField(max_length = 150)
    expected_salary= models.CharField(max_length = 150)
    cv= models.FileField(upload_to='ApplicationCV')
    message = models.TextField()
    
    def __str__(self):
        return self.email



class News_and_Evenet(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='NewsAndEvenetImage')
    description =RichTextUploadingField()
    
    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='NewsAndEvenetImage')
    description =RichTextUploadingField()
    
    def __str__(self):
        return self.title

class MissionVission(models.Model):
    Object_type =(
        ('mission','mission'),
        ('vission','vission')
    )
    title = models.CharField(max_length = 150)
    object_type = models.CharField(max_length = 150, choices=Object_type)
    image = models.ImageField(upload_to='MissionVissionImg')
    description =RichTextUploadingField()
    
    def __str__(self):
        return self.title

class IT_Profile(models.Model):
    title = models.CharField(max_length = 150)
    it_profile_file= models.FileField(upload_to='ItProfileFile')

    def __str__(self):
        return self.title
    

    
    