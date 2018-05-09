from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "projects": reverse('project-list', request=request, format=format),
    })

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
