from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf.urls import include, url
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^predict_test_set/$', views.predict_test_set, name="predict_test_set"),
    url(r'^$', views.home, name="home"),
    url(r'^pred_one/$', views.pred_one, name="pred_one"),
    url(r'^pred_one_result/$', views.pred_one_result, name="pred_one_result"),
    url(r'^viz/$', views.viz, name="viz"),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/images/favicon.ico')),

]
