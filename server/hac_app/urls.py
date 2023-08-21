from django.urls import path

from .views import AboutView


app_name = 'hac_app'

urlpatterns = [
    path("about/", AboutView.as_view(), name='about'),
]
