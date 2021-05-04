from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ImageUpdateForm ,RegisterForm, LoginForm, youtube_form,instagram_form,twitter_form,facebook_form,spotify_form,soundcloud_form, interests_form, UserUpdateForm, email_form, phone_form
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import Profile, Relationship, RelationshipManager
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q





########## PROFILE IMAGE UPDATE ###################
@login_required(login_url = "user:login")
def update_image(request,id):
    if request.method == "POST":
        Image_form = ImageUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if Image_form.is_valid():
            Image_form.save()
    else:
        Image_form = ImageUpdateForm(instance=request.user.profile) 
    forms = {
        "Image_form" :Image_form,
    }
    return render(request,"updateimage.html", {"forms":forms} )


############## UPDATE PROFILE ##############
@login_required(login_url = "user:login")
def update_profile(request,id):
    profile1 = get_object_or_404(Profile, id = id)
    interests_form1 = interests_form(request.POST or None, instance = profile1)
    youtube_form1 = youtube_form(request.POST or None, instance = profile1)
    instagram_form1 = instagram_form(request.POST or None, instance = profile1)
    twitter_form1 = twitter_form(request.POST or None, instance = profile1)
    facebook_form1 = facebook_form(request.POST or None, instance = profile1)
    spotify_form1 = spotify_form(request.POST or None, instance = profile1)
    soundcloud_form1 = soundcloud_form(request.POST or None, instance = profile1)
    email_form1 = email_form(request.POST or None, instance = profile1) 
    phone_form1 = phone_form(request.POST or None, instance = profile1) 

    if request.method=='POST': #and 'interests' in request.POST:
        if interests_form1.is_valid():
            profile1 = interests_form1.save(commit=False)
            profile1.save()
        if youtube_form1.is_valid():
            profile1 = youtube_form1.save(commit=False)
            profile1.save()
        if instagram_form1.is_valid():
            profile1 = instagram_form1.save(commit=False)
            profile1.save()       
        if facebook_form1.is_valid():
            profile1 = facebook_form1.save(commit=False)
            profile1.save()       
        if twitter_form1.is_valid():
            profile1 = twitter_form1.save(commit=False)
            profile1.save()       
        if spotify_form1.is_valid():
            profile1 = spotify_form1.save(commit=False)
            profile1.save()       
        if soundcloud_form1.is_valid():
            profile1 = soundcloud_form1.save(commit=False)
            profile1.save()    
        if email_form1.is_valid():
            profile1 = email_form1.save(commit=False)
            profile1.save()   
        if phone_form1.is_valid():
            profile1 = phone_form1.save(commit=False)
            profile1.save()      
        return redirect(reverse("user:update_profile",kwargs={"id":id}))
        profile1.user = request.user
        profile1.save()
    
    forms = {
        "interests_form1" :interests_form1,
        "youtube_form1" : youtube_form1,
        "instagram_form1" : instagram_form1,
        "twitter_form1" : twitter_form1,
        "facebook_form1" : facebook_form1,
        "spotify_form1" : spotify_form1,
        "soundcloud_form1" : soundcloud_form1,
        "phone_form1" : phone_form1,
        "email_form1" : email_form1,
    }
    return render(request,"update_profile.html", {"forms":forms} )





########## REGISTER USER ###################
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username =username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)



########## LOGIN USER ###################
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
        #    messages.info(request,"Incorrect username or password")
            return render(request,"login.html",context)
        #messages.success(request,"Logged in successfully")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


########## LOGOUT USER ###################
def logoutUser(request):    
    logout(request)
    #messages.success(request,"Logged out successfully")
    return redirect("index")


############## USER PROFILE - PRIVATE PAGE ##############
def view_profile(request):
    profile = Profile.objects.filter(user = request.user)[0]
    return render(request,"profile.html", {"profile":profile})


############## USER PROFILE - PUBLIC PAGE ##############
def public_profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    return render(request,"publicprofile.html", {"profile":profile})



################## INVITATIONS PAGE ###################
def friends_invites(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True
    context = { "qs":results,
                "profile":profile,
                "is_empty": is_empty,
                }
    print(qs)
    return render(request, "friends_invites.html", context)


################ ACCEPT AND REJECT INVITATION ########################
def accept_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == "send":
            rel.status = "accepted"
            rel.save() 
    return redirect('user:allprofiles')

def reject_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete() 
    return redirect('user:allprofiles')





################# PROFILES AVAILABLE FOR INVITE #######################
def inviteprofiles(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)
    context = { "qs":qs,
               }
    return render(request, "inviteprofiles.html", context)

################# ALL PROFILES #######################
def allprofiles(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    context = { "qs":qs,
               }
    return render(request, "allprofiles.html", context)

class ProfileListView(ListView):
    model = Profile
    template_name = "allprofiles.html"
    context_object_name ="qs"

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)        
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context["is_empty"] = False
        if len(self.get_queryset()) == 0:
            context["is_empty"] = True
        return context

#####################################

def send_invitation(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)
        rel = Relationship.objects.create(sender=sender, receiver=receiver, status="send")
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect('user:allprofiles')

def remove_from_friends(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender)) )
        rel.delete()
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect('user:allprofiles')

