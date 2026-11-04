from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    path("project/", api_views.project_list, name="project-list"),
    path("project/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("project/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
]