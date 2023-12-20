"""
URL configuration for bookworks project.

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
from crm import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/add',views.BookCreateView.as_view(),name="book-add"),
    path('book/all',views.BooklistView.as_view(),name="book-list"),
    path('book/<int:pk>',views.BookDetailView.as_view(),name="book-detail"),
    path('book/<int:pk>/change',views.BookUpdateView.as_view(),name="book-update"),
    path('book/<int:pk>/remove',views.BookDeleteView.as_view(),name="book-remove"),
    path('signup',views.SignupView.as_view(),name="signup"),
    path('',views.SigninView.as_view(),name="signin"),
    path('logout',views.SignOutView.as_view(),name="logout")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
