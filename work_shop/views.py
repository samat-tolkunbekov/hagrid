from django.http import HttpResponse, JsonResponse
from .playground import Playground

def index(request):
    return JsonResponse({"ok": True}, safe=False)

def about(request):
    return JsonResponse({"ok": True}, safe=False)

def contact(request):
    return JsonResponse({"ok": True}, safe=False)

def api_data(request):
    return JsonResponse(Playground().get_data(), safe=False)

def api_data_detail(request, data_id):
    # Your API data detail retrieval logic here
    return JsonResponse({"ok": True}, safe=False)
