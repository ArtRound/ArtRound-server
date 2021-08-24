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


def update(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    if request.method == 'POST':
        update_form = WriteForm(request.POST, instance=my_write)

        if update_form.is_valid():
            update_form.save()
            return redirect('index')

    update_form = WriteForm(instance=my_write)
    return render(request, 'update.html', {'update_form': update_form})


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')
