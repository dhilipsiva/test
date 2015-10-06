from django.http import JsonResponse

from core.models import Project


def projects(request):
    """
    List projects
    """
    projects = [project.to_dict() for project in Project.objects.all()]
    return JsonResponse({"projects": projects})


def project(request, uuid):
    """
    Get a single project
    """
    project = Project.objects.get(uuid=uuid)
    return JsonResponse(project.to_dict())
