from django.urls import re_path
from helloworld import views
urlpatterns = [
    re_path(r"hello-world/$", views.first_view_func)
]
