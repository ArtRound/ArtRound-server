from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

from django.shortcuts import get_object_or_404, redirect, render
from .forms import WriteForm
from .models import Write


def index(request):
    all_write = Write.objects.all()
    return render(request, 'index.html', {'all_write': all_write})


def create(request):
    if request.method == 'POST':
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
        return redirect('index')
    write_form = WriteForm
    return render(request, 'create.html', {'write_form': write_form})


def detail(request, write_id):
    my_write = get_object_or_404(Write, pk=write_id)

    return render(request, 'detail.html', {'my_write': my_write})


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')
