from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Juan Imanuel Limpong",
        "npm": "2506619455",
        "study_program": "Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia with a strong interest in"
            "technology, such as digial product design."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Juan Imanuel Limpong",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Juan Imanuel Limpong",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)