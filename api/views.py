from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializers, ProjectcreateSerializers
from projects.models import Project


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializers(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def createProject(request):
    owner = request.user.profile
    project = Project.objects.create(owner=owner)

    serializer = ProjectcreateSerializers(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
