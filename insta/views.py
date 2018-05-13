from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title = 'Insta-Gram'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'index.html',{"title":title,
                                        "profile":profile,
                                        "comments":comments,
                                        "current_user":current_user,
                                        "images":image,})
