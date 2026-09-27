from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminapp.models import Admin,Room

def login(request):
    if request.method == 'POST':

        email= request.POST.get("email")
        password = request.POST.get("password")

        admin = Admin.objects.filter(
        email = email,
        password = password).first()
        if(admin):
            request.session["admin_id"] = admin.id
            request.session["admin_name"] = admin.username
            request.session["admin_email"] = admin.email
            return redirect("admin_dashboard_link")
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request,"adminapp/login.html")

def dashboard(request):
    admin_name = request.session.get("admin_name")
    return render(request, "adminapp/dashboard.html",{"admin_name":admin_name})

def adminprofile(request):
    admin_id = request.session.get("admin_id")
    admin = Admin.objects.get(id = admin_id)
    return render(request, "adminapp/admin_profile.html", 
        {"admin":admin})

def adminprofileupdate(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        admin_pic = request.FILES.get("admin_pic")

        admin_id = request.session.get("admin_id")

        admin = Admin.objects.get(id=admin_id)

        admin.username = username
        admin.email = email
        admin.phone = phone

        if admin_pic:
            admin.admin_pic = admin_pic

        admin.save()

        return redirect("admin_profile_update_link")

    else:
        return render(request, "adminapp/admin_profile_update.html")

def addRoom(request):
  if request.method=="POST":
    room_no = request.POST.get("room_no")
    floor = request.POST.get("floor_no")
    room_type = request.POST.get("room_type")
    bed_no = request.POST.get("bed_no")
    rent = request.POST.get("rent")
    description = request.POST.get("description")
    rating = request.POST.get("rating")
    review = request.POST.get("review")
    status = request.POST.get("status")
    room_image = request.FILES.get("room_image")
    
    Room.objects.create(
      room_no = room_no,
      floor = floor,
      room_type = room_type,
      total_beds = bed_no,
      monthly_rent = rent,
      description = description,
      rating=rating,
      review=review,
      status=status,
      room_image = room_image
    )
    return redirect("admin_dashboard_link")
  else:
    return render(request,"adminapp/add_room.html")