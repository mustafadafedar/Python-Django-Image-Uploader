from django.shortcuts import render
from .forms import imageform
from .models import upload
# Create your views here.

def main(request):
    if request.method == 'POST':
        form = imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = imageform()
    img = upload.objects.all()
    return render(request,'index.html',{'img':img,'form':form})