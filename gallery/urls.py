from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root, name='api-root'),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail')
])

'''
urlpatterns = format_suffix_patterns([
    path('', views.api_root, name='api-root'),
    path('sites/', views.SitesList.as_view(), name='sites-list'),
    path('software/', views.SoftwareList.as_view(), name='software-list'),
    path('games/', views.GamesList.as_view(), name='games-list'),
    path('sites/<int:pk>/', views.SitesDetail.as_view(), name='project-detail'),
    path('software/<int:pk>/', views.SoftwareDetail.as_view(), name='project-detail'),
    path('games/<int:pk>/', views.GamesDetail.as_view(), name='project-detail'),
])
'''