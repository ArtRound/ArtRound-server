from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')
