# from django.http import HttpResponse,httpResponseRedirect
from django.shortcuts import render,redirect
from .models import Image,Profile,Rates
from django.contrib.auth.decorators import login_required
from .forms import Form,NewImageForm,UpdateProForm,RateForm
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ImageSerializer
# Create your views here.



def index(request):
    # date = dt.date.today()
    image_pic = Image.objects.all()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Recipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
    else:
        form = Form()
    return render(request, 'index.html', {"NewImageForm":form,"image_pic":image_pic})

@login_required(login_url='/accounts/login/')
def new_pic(request):
    current_user = request.user
    profile = Profile.objects.filter(user_name=current_user).first()
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user_name = current_user
            picture.profiles = profile
            picture.save()
        return redirect('addPic')

    else:
        form = NewImageForm()
    return render(request, 'everything/add-pic.html', {"form": form})

@login_required(login_url='/accounts/login/')
def getProfile(request,users=None):
    user = request.user
    image_pic = Image.objects.filter(user_name=user)
    user_name = request.user
    profile = Profile.objects.filter(user_name=user_name).first()
    
    return render(request,'everything/profile.html',locals(),{"image_pic":image_pic})


@login_required(login_url='/accounts/login/')
def editProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProForm(request.POST,request.FILES)
        if form.is_valid():
            pics = form.save(commit=False)
            pics.user_name = current_user
            pics.save()
        return redirect('profile')

    else:
        form = UpdateProForm()
    return render(request,'everything/pro_edit.html',{"test":form})

def search(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        pictures = Image.search_by_ciro(search_term)
        message = f"{search_term}"

        return render(request, 'everything/search.html',{"message":message,"pictures": pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'everything/search.html',{"message":message, "pictures": pictures})

# rating code from nyota245 github
@login_required
def rating(request):
    '''
    Function to display single Project and rate it
    '''
    current_user = request.user
    projects = Image.objects.filter().first()
    title = "Rating"
    project_rating = Rates.objects.filter(pic=projects).order_by("pk")
    current_user = request.user.id
    project_rated = Rates.objects.filter(user_name=current_user)


    design_mean_rating = []
    for d_rating in project_rating:
        design_mean_rating.append(d_rating.design)
    try:
        designav = sum(design_mean_rating)/len(design_mean_rating)
        designper = design_average * 10
    except ZeroDivisionError:
        designav = "0"
        designper = 0

    usability_mean_rating = []
    for u_rating in project_rating:
        usability_mean_rating.append(u_rating.usability)
    try:
        usabilityav = sum(usability_mean_rating)/len(usability_mean_rating)
        usabilityper = usability_average *10
    except ZeroDivisionError:
        usabilityav = "0"
        usabilityper = 0
    
    content_mean_rating = []
    for c_rating in project_rating:
        content_mean_rating.append(c_rating.content)
    try:
        contentav = sum(content_mean_rating)/len(content_mean_rating)
        contentper = content_average * 10
    except ZeroDivisionError:
        contentav = "0"
        contentper = 0

    form = RateForm()

    context = {
        "projects":projects,
        "form":form,
        "project_rating":project_rating,
        "designav":designav,
        "contentav":contentav,
        "usabilityav":usabilityav,
        "usabilityper":usabilityper,
        "contentper":contentper,
        "designper":designper
    }

    return render(request,"rates.html",context)




class ImageList(APIView):
    def get(self,request,format=None):
        projects = Image.objects.all()
        serializers = ImageSerializer(projects,many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self,request,format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)