from django.shortcuts import get_object_or_404,redirect,render
from django.contrib.auth.models import User
from .models import Photo

def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    params = {
        'photos':photos
    }
    return render(request, 'app/index.html',params)

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    params = {
        'user':user,
    }
    return render(request,'app/users_detail.html',params)