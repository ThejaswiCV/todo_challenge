"""
URL configuration for todotask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignUpView.as_view(),name="sign_up"),
    path('signin',views.signInView.as_view(),name="sign_in"),
    path('index',views.IndexView.as_view(),name='index'),
    path('project/<int:pk>',views.ProjectView.as_view(),name='project_detail'),
    path('project/<int:pk>/remove',views.ProjectDeleteView.as_view(),name='project_delete'),
    path('project/<int:pk>/delete',views.TodoDeleteView.as_view(),name='todo_delete'),
    path('project/<int:pk>/status',views.TodoStatusView.as_view(),name='todo_status'),
    path('project/<int:pk>/update_todo',views.UpdateTodoView.as_view(),name='update_todo'),
    path('signout',views.LogoutView.as_view(),name="sign_out"),
    path('export-gist/<int:pk>', views.ExportGistView.as_view(), name='export_gist'),
    path('project/<int:pk>/change_title', views.ProjectTitleView.as_view(), name='update_project_title')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
