from django.urls import path
# import students.views as views
from . import views

urlpatterns = [
    path('', views.home_view, name='home')
    , path('submit/', views.submitButton, name='submitButton')
    , path('clear/', views.clearStudentsButton, name='clearButton')
]