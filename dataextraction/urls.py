# howdy/urls.py
from django.conf.urls import url
from dataextraction import views


urlpatterns = [
    url(r'^$', views.form_name_view.as_view()),
]