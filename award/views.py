from django.shortcuts import render,redirect
from .models import Projects,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,UpdateProForm

# Create your views here.
def index(request):
    # date = dt.date.today()
    image_pic = Projects.objects.all()

    return render(request, 'index.html', {"image_pic":image_pic})