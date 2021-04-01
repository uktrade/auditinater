from django.http import HttpResponse


def index(request):
    """A super basic site root rather than 400 bad request.
    """
    return HttpResponse("🚀 auditinater 🚀")
