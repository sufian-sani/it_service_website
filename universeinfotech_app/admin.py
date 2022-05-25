from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Banner_Slider)
admin.site.register(ClientsReview)
admin.site.register(Tools)
admin.site.register(Portfolio)
admin.site.register(Our_Client)
admin.site.register(News_and_Evenet)
admin.site.register(Notice)
admin.site.register(MissionVission)
admin.site.register(IT_Profile)


class CareerAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('title',)}
admin.site.register(Career,CareerAdmin)


class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Feature, FeatureAdmin)


class Our_ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Our_Service,Our_ServiceAdmin)


class Project_GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Project_Gallery,Project_GalleryAdmin)


class Developer_ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Developer_Profile,Developer_ProfileAdmin)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Blog,BlogAdmin)