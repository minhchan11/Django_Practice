from django.urls import path,include,re_path
from howdy import views

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('about/', views.AboutPageView.as_view())
]
