from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('philosophy/', views.philosophy, name='philosophy'),
    path('bim/', views.bim, name='bim'),

    path('buying-mistakes/', views.buying_mistakes, name='buying-mistakes'),
    path('architecture-and-nature/', views.architecture_and_nature, name='architecture-and-nature'),
    path('prototyping/', views.prototyping, name='prototyping'),
    path('entry-group/', views.entry_group, name='entry-group'),
    path('architectural-style/', views.architectural_style, name='architectural-style'),
    path('finished-projects/', views.finished_projects, name='finished-projects'),








    path('projects/residential-complex-in-nakhodka/', views.projects_sample),
    path('projects/river-park/', views.projects_sample),
    path('projects/modern-house/', views.projects_sample),
    path('projects/block-house/', views.projects_sample),
    path('projects/aljans/', views.projects_sample),
    path('projects/one-story-house/', views.projects_sample),
    path('projects/two-story-house/', views.projects_sample),
    path('projects/recreation-center-in-krasno/', views.projects_sample),
    path('projects/house-in-cottage-village/', views.projects_sample),
    path('projects/administrative-building/', views.projects_sample),
    path('projects/frame-house/', views.projects_sample),
    path('projects/high-tech/', views.projects_sample),
    path('projects/one-story-house-in-vladivostok/', views.projects_sample),



    path('service/individual-housing-construction/', views.individual_housing_construction, name='individual_housing_construction'),
    path('service/preproject/', views.pre_project, name='pre_project'),
    path('service/fasad/', views.fasad, name='fasad'),
    path('service/commercial/', views.commercial, name='commercial'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
