from rest_framework import serializers
from .models import Project, Picture, Video


class PictureSerializer(serializers.ModelSerializer):
    screenshot_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Picture
        fields = ('project', 'screenshot_thumbnail','screenshot',)


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('project', 'video',)


class ProjectSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'category',
            'title',
            'slug_title',
            'description',
            'url',
            'created',
            'pictures',
            'videos')
