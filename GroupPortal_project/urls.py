"""
URL configuration for GroupPortal_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
     . Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
     . Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
     . Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #    MAIN PAGE   
    path('', include('MainPage_app.urls')),

    #    AUTHENTICATION   

    path('auth/', include('Authentication_app.urls')),

    #    FORUM   
    path('categoryes/', include('Forum_app.urls')),

    #    ELECTRONIC DIARY (students / teachers / classes / etc.)   
    path('', include('ElectronicDiary_app.urls')),

    #     EVENTS 
    path('events/', include('Events_app.urls')),

    #    MATERIALS   
    path('materials/', include('Materials_app.urls')),

    #  QUESTIONS SYSTEM  
    path('questions/', include('QuestionsSystem_app.urls')),

    #    VOTING SYSTEM   
    path('voting/', include('VotingSystem_app.urls')),

    #    GALLERY   
    path('albums/', include('Gallery_app.urls')),

    #    PORTFOLIO   
    path('portfolio/', include('Portfolio_app.urls')),

    #    ADVERTISEMENTS   
    path('advertisements/', include('Advertisement_app.urls')),
    path('listes/', include('Advertisement_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
