from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminapp.models import Admin,Room,Notice

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
    if "admin_name" not in request.session:
       return redirect("admin_login_link")
    admin_name = request.session.get("admin_name")
    rooms = Room.objects.all()
    return render(request,"adminapp/dashboard.html",
    {"admin_name":admin_name,"rooms":rooms})

def adminprofile(request):
    if "admin_name" not in request.session:
        return redirect("admin_login_link")
    admin_id = request.session.get("admin_id")
    admin = Admin.objects.get(id = admin_id)
    return render(request, "adminapp/admin_profile.html", 
        {"admin":admin})

def adminprofileupdate(request):
    if "admin_name" not in request.session:
        return redirect("admin_login_link")
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
  if "admin_name" not in request.session:
    return redirect("admin_login_link")
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

# def roomDetail(request,id):
#   if "admin_name" not in request.session:
#     return redirect("admin_login_link")
#   room = Room.objects.get(id = id)
#   return render(request,"adminapp/room_detail.html",{"room":room})

def roomDetail(request, id):
    room = Room.objects.get(id=id)
    if "admin_name" in request.session:
        dashboard_url = "admin_dashboard_link"

    elif "user_id" in request.session:
        dashboard_url = "user_dashboard_link"

    else:
        return redirect("user_login_link")

    return render(
        request,
        "adminapp/room_detail.html",
        {
            "room": room,
            "dashboard_url": dashboard_url
        }
    )

def notice(request):
  if "admin_name" not in request.session:
    return redirect("admin_login_link")
  if request.method == "POST":
    title = request.POST.get("title")
    description = request.POST.get("description")
    Notice.objects.create(title=title,description=description)
    return redirect("notice_link")
  else:
    notice = Notice.objects.all().order_by("-created_at")
    return render(request,"adminapp/notice.html",{"notice":notice})

def logout(request):
   request.session.flush()
   return redirect("admin_login_link")