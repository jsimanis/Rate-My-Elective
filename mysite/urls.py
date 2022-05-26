"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from website import views
from django.contrib.auth import views as auth_views

admin.site.site_header = 'RateMyElective Admin'

urlpatterns = [
    # Standard built-in url endpoints
    path('admin/', admin.site.urls),

    # Core functionality url endpoints
    path('', views.home, name="home"),
    path('elective/<str:department>/<int:classNum>', views.elective, name="elective"),
    path('elective/<str:department>/<int:classNum>/flag', views.flag_review, name="flag_elective"), # flag a review
    path('elective/<str:department>/<int:classNum>/delete_review', views.delete_review, name="delete_review"),
    path('contact/', views.contact, name="contact"),
    path('contact_confirm/', views.contactconfirm, name="contactconfirm"),
    path('search_results/', views.search, name= "search_results"),
    path('add_class/', views.addClass, name= "add_class"),
    path('add_dept/', views.addDept, name="add_dept"),

    path('register/', views.registerUser, 
    name="registerUser"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('profile/', views.profile, name="profile"),
    path('profile/delete_account', views.delete_account, name="delete_account"),
    path('flagreview/', views.flag_review, name="flag_review"),

    # Password reset url endpoints
    path('reset-password/',
         auth_views.PasswordResetView.as_view
         (template_name="password_reset.html"),
         name="reset_password"),
    path('reset-password-sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view
         (template_name="password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view
         (template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
