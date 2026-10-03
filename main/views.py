import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

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
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Juan Imanuel Limpong",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)


def show_education(request):
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Juan Imanuel Limpong",
        "institution_query": institution_query,
        "form": EducationForm(),
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
    if not request.user.has_perm("main.change_project"):
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


@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.has_perm("main.change_education"):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    form = ProjectForm(
        request.POST or None,
        instance=project
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated successfully.")
        return redirect("main:show_projects")

    context = {
        "name": "Juan Imanuel Limpong",
        "form": form,
        "project": project,
    }

    return render(request, "projects_form.html", context)



def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Kontruksi data JSON secara manual agar bisa menyisipkan Logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "category": project.category,
                "project_url": project.project_url,
                "thumbnail": project.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()

    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)

    data = []
    for education in educations:
        data.append({
            "pk": str(education.id),
            "fields": {
                "institution": education.institution,
                "degree": education.degree,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "description": education.description,
            }
        })

    return JsonResponse(data, safe=False)


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


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portofolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )
    return JsonResponse({"error": form.errors.get_json_data()}, status=400)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portofolio owner can add educations."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education added successfully.", "pk": str(education.id)},
            status=201,
        )
    return JsonResponse({"error": form.errors.get_json_data()}, status=400)