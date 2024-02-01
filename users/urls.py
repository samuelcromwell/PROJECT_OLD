from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('login/', views.login, name="login"),
    path('courses/', views.courses, name="courses"),
    path('signup/', views.signup, name="signup"),
    path('admin/', views.admin, name="admin"),
    path('traineelogin/', views.traineelogin, name="traineelogin"),
]
