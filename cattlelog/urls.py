from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.log,name='log'),
    url(r'^fulldetail',views.fulldetail,name='fulldetail'),
    url(r'^ramudetail',views.ramudetail,name='ramudetail'),
]
