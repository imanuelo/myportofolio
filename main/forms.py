from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from main.models import Project, Education

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
                    "placeholder": "https://drive.google.com/thumbnail...sz1000",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "start_year",
            "end_year",
            "description",
        ]

        labels = {
            "institution": "Institution",
            "degree": "Degree / Major",
            "start_year": "Start Year",
            "end_year": "End Year",
            "description": "Description",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "School or University",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Major or Study Program",
                    "maxlength": 255,
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2024",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your education",
                    "rows": 3,
                }
            )
        }