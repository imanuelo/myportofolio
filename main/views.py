from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project, Education
from main.forms import ProjectForm, EducationForm

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
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Juan Imanuel Limpong",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)


def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Juan Imanuel Limpong",
        "education_list": educations,
        "institution_query": institution_query
    }
    return render(request, "education.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Project has been added!")
        return redirect("main:show_projects")

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Education added successfully.")
        return redirect("main:show_education")

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
    }
    return render(request, "education_form.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")


def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    form = EducationForm(
        request.POST or None,
        instance=education
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education updated successfully.")
        return redirect("main:show_education")

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
        "education": education,
    }

    return render(request, "education_form.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    project_json = serializers.serialize("json", projects)
    return HttpResponse(project_json, content_type="application/json")


def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    institution_json = serializers.serialize("json", educations)
    return HttpResponse(institution_json, content_type="application/json")