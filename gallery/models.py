from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


def directory_path(instance, filename):
    #file will be uploaded to MEDIA_ROOT/<project.slug_header>/<filename>
    return '{0}/{1}'.format(instance.project.slug_title, filename)


class Project(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=300, blank=True)
    slug_title = models.SlugField(max_length=300, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    url = models.URLField(verbose_name="Адрес сайта",blank=True)
    created = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    category_choices = (
        ("sites", 'Сайты'),
        ("games", 'Игры'),
        ("software", 'Софт'),
    )
    category = models.CharField(
        verbose_name="Категория",
        max_length=30,
        choices=category_choices,
        default="sites",
        blank=True
    )

    def __str__(self):
        return self.slug_title


class Picture(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='pictures')
    screenshot = models.ImageField(
        verbose_name="Скриншоты проекта",
        upload_to=directory_path,
        help_text="Загрузите изображение",
        blank=True)
    screenshot_thumbnail = ImageSpecField(
        source='screenshot',
        processors=[ResizeToFill(250, 200)],
        format='JPEG',
        options={'quality': 80})


class Video(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='videos')
    video = models.URLField(verbose_name="Видео", blank=True)