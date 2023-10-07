
from django.contrib import admin
from django.urls import path

from djangoProject.myFunc import aboutData, getData, getaddress, getHistory, connect2, getChartData, home, deleteData, \
    insertData, inData, basketData, inDataContract, getServices, getSlider, getFunfact, getMenu, getAbout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("getdata/", getData),
    path("getaddress/", getaddress),
    path("getHistory/", getHistory),
    path("register/", connect2),
    path("getChartData/", getChartData),
    path("home/", home),
    path("about/", aboutData),
    path("delete/", deleteData),
    path("insert/", insertData),
    path("inData", inData),
    path("serverData/", basketData),
    path("insertContact/", inDataContract),
    path("getServices/", getServices),
    path("getSlider/", getSlider),
    path("getFunfact/", getFunfact),
    path("getMenu/", getMenu),
    path("getAbout/", getAbout),
]
