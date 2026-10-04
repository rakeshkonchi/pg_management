from django.shortcuts import render,redirect
from django.http import HttpResponse
from userapp.models import User,UserProfile
from adminapp.models import Room

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        User.objects.create(username=username,email=email,phone=phone,password=password)
        return redirect("user_signup_link")
    else:
        return render(request,"userapp/signup.html")

def user_login(request):
    if request.method == 'POST':

        email= request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(
        email = email,
        password = password).first()
        if(user):
            request.session["user_id"] = user.id
            request.session["user_name"] = user.username
            request.session["user_email"] = user.email
            return redirect("user_dashboard_link")
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request,"userapp/login.html")

def user_dashboard(request):
    if "user_id" not in request.session:
        return redirect("user_login_link")
    username = request.session.get("user_name")
    rooms = Room.objects.all()
    return render(request,"userapp/user_dashboard.html",
    {"username":username,"rooms":rooms})

def user_profile(request):

    if "user_id" not in request.session:
        return redirect("user_login_link")

    user_id = request.session.get("user_id")

    user = User.objects.get(id=user_id)

    return render(
        request,
        "userapp/user_profile.html",
        {
            "user": user
        }
    )

def user_profile_update(request):
    if "user_id" not in request.session:
        return redirect("user_login_link")
    if request.method == "POST":
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        state = request.POST.get("state")
        country = request.POST.get("country")
        address = request.POST.get("address")
        bio = request.POST.get("bio")
        aadhar_no = request.POST.get("aadhar_no")
        aadhar_image = request.FILES.get("aadhar_image")
        profile_pic = request.FILES.get("profile_pic")

        user_id = request.session.get("user_id")
        user = User.objects.get(id=user_id)

        UserProfile.objects.create(
            user=user,
            city=city,
            pincode=pincode,
            state=state,
            country=country,
            address=address,
            bio=bio,
            aadhar_no=aadhar_no,
            aadhar_image=aadhar_image,
            profile_pic=profile_pic
        )     
        return redirect("user_profile_link")
    
    return render(request, "userapp/user_profile_update.html")