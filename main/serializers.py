from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Education


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "category",
            "project_url", "thumbnail",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_category(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())



class EducationSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = [
            "id", "institution", "degree",
            "start_year", "end_year", "description",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names",]

    def validate_institution(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Institution cannot be empty.")
        return value

    def validate_degree(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Degree cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate_start_year(self, value):
        if value < 2000:
            raise serializers.ValidationError("Start year must be at least 2000.")
        return value

    def validate_end_year(self, value):
        if value < 2000:
            raise serializers.ValidationError("End year must be at least 2000.")
        return value

    def validate(self, data):
        start_year = data.get("start_year", getattr(self.instance, "start_year", None))
        end_year = data.get("end_year", getattr(self.instance, "end_year", None))
        if end_year < start_year:
            raise serializers.ValidationError({"end_year": "End year cannot be earlier than start year."})
        return data

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(pk=request.user.pk).exists()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())