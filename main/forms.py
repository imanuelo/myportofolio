from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
            "project_url",
            "thumbnail",
        ]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "category": "Type of Project",
            "project_url": "Link Project",
            "thumbnail": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portofolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "About Your Project",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "UI/UX Design, Web Design, App Design"
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "Link Project"
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail...",
                }
            ),
        }