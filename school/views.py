from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def sample_url(request):
    return Response({"message": "Hello, world!"})
