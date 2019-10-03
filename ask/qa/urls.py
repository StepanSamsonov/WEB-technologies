from django.conf.urls import url
from . import views


urlpatterns = [
    url('/', views.test),
    url('/login/', views.test),
    url('/signup/', views.test),
    url('/question/<int:id>/', views.test),
    url('/ask/', views.test),
    url('/popular/', views.test),
    url('/new/', views.test),
]
