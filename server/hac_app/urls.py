from django.urls import path

from .views import *


app_name = 'hac_app'

urlpatterns = [
    path("about/", AboutView.as_view(), name='about'),
    path("index/", IndexView.as_view(), name='index'),
    path("main/", MainView.as_view(), name='main'),
    path("header/", HeaderView.as_view(), name='header'),
    path("footer/", FooterView.as_view(), name='footer'),
    path("chart/", ChartView.as_view(), name='chart'),
    path("form/", FormView.as_view(), name='form'),
    path("contacts/", ContactsView.as_view(), name='contacts'),
    path("form-and-chart/", FormAndChartView.as_view(), name='form-and-chart'),
    path("simple-page/", SimplePageView.as_view(), name='simple-page'),
    path("one-string/", OneStringView.as_view(), name='one-string'),
    path("req-file/", ReqFileView.as_view(), name='one-string'),
    path("download/", DownloadView.as_view(), name='download'),
]
