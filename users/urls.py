from django.urls import path

from . import views

urlpatterns = [
    path("profile/", views.user_profile),
    path("cohort/", views.get_cohort),
    path("user/", views.get_user),
    path("cohortmember/", views.get_cohort_member),
]
