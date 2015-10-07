from django.http import JsonResponse

from core.models import Project, File, Page


def projects(request):
    """
    List projects
    """
    projects = [project.to_dict() for project in Project.objects.all()]
    return JsonResponse({"projects": projects})


def project(request, project_uuid):
    """
    Get a single project
    """
    project = Project.objects.get(uuid=project_uuid)
    return JsonResponse({"project": project.to_dict()})


def files(request):
    """
    docstring for files
    """
    project_uuid = request.GET.get("uuid")
    files = File.objects.filter(project__uuid=project_uuid)
    return JsonResponse({"files": [f.to_dict() for f in files]})


def file(request, file_uuid):
    """
    Get a single project
    """
    file = File.objects.get(uuid=file_uuid)
    return JsonResponse({"file": file.to_dict()})


def pages(request):
    """
    docstring for files
    """
    file_uuid = request.GET.get("uuid")
    pages = Page.objects.filter(file__uuid=file_uuid)
    return JsonResponse({"pages": [p.to_dict() for p in pages]})
