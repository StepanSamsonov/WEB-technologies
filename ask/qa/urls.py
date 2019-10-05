from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.page),
    url(r'^login', views.test),
    url(r'^signup', views.test),
    url(r'^question/<int:id>', views.question_page),
    url(r'^ask', views.test),
    url(r'^popular', views.popular_page),
    url(r'^new', views.test),
]
