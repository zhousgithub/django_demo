from django.conf.urls import url
from django.contrib import admin

from demo.cpws import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^insert/', views.insert),

]