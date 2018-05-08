from rest_framework import serializers
from .models import Project, Picture, Video


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('screenshot_thumbnail', 'screenshot',)


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('video',)


class ProjectSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('category', 'header', 'slug_header', 'description', 'url', 'created', 'pictures', 'videos')
