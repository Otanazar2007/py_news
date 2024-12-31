"""
URL configuration for this_is_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from this_is_app.views import home_page, comment_view, add_comment, comment, like, submit_news, predlojen_new
from django.conf import settings
import user.views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name = 'home'),
    path('registration/', user.views.register_view, name = 'registration'),
    path('login/', user.views.login_view, name = 'login'),
    path('commentary/', comment_view, name = 'commentary'),
    path('comment/<int:pk>', comment, name = 'comment_from_post'),
    path('comment/add_comment/<int:pk>',add_comment, name = 'add_comment'),
    path('like/<int:pk>',like, name = 'add_to_likes'),
    path('predlojeniye_novosta/', predlojen_new, name = 'predlojenie_novosta'),
    path('submit_news/', submit_news, name = 'submit_news')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)