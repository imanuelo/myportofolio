import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project, Education
from main.forms import ProjectForm, EducationForm

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session / Cookie not found')
    context = {
        "name": "Juan Imanuel Limpong",
        "npm": "2506619455",
        "study_program": "Sistem Informasi",
        "bio": (
            "Information Systems student at Universitas Indonesia with a strong interest in"
            "technology, such as digial product design."
        ),
        "last_login": last_login
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project has been deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")


@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")


@login_required(login_url="/login/")
def update_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

    project_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(project_json, content_type="application/json")


def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    institution_json = serializers.serialize("json", educations)
    return HttpResponse(institution_json, content_type="application/json")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response