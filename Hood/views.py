from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User_profile,Post,Neigbourhood,Business
from django.contrib.auth.decorators import login_required
from .forms import UploadForm

@login_required(login_url='/accounts/login/') 
def index(request):
    
    update= Post.objects.all()

    return render(request,'temps/index.html',{"update":update})
    
  
@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    title = 'Mtaa | Upload'
    profiles = User_profile.get_profile()
    for profile in profiles:
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.profile = profile
            upload.save()
            
            return redirect('post')
            messages.success(request, 'Status  updated '\
                                      'successfully')
        else:
            form = UploadForm()
    return render(request,'temps/upload.html',{"title":title, "user":current_user,"form":form})

@login_required(login_url='/accounts/login/')    
def post(request):
    current_user = request.user
    update= Post.objects.all()
    return render(request,'temps/post.html',{"update":update,"user":current_user})
  

def group(request):
    
    group=Neigbourhood.objects.all()

    return render(request,'temps/group.html',{'group':group})  


def search_results(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business = Business.search_biz(search_term)
        message = f"{search_term}"

        return render(request, 'temps/search.html',{"message":message,"business": business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'temps/search.html',{"message":message})    

@login_required(login_url='/accounts/login/')        
def single_profile(request):
    current_user=request.user
    profiles=User_profile.objects.all()
    return render(request,'temps/userprof.html',{"profiles":profiles,"user":current_user})