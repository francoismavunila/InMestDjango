from django.urls import path

from . import views

urlpatterns = [
    path("say_hello/", views.say_hello),
    path("filter/<int:id>/", views.filter_queries),
    path("queries/", views.QueryView.as_view()),
]
