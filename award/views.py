from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # date = dt.date.today()
    image_pic = Projects.objects.all()

    return render(request, 'index.html', {"image_pic":image_pic})