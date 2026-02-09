from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from securityapp.models import*

# Create your views here.def index(request):
def index(request):
    return render(request, "index.html", locals())

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

def hiring_form(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobileno = request.POST['mobileno']
        email = request.POST['email']
        address = request.POST['address']
        requirementnumber = request.POST['requirementnumber']
        shift = request.POST['shift']
        gender = request.POST['gender']
        bookingnumber = random_with_N_digits(8)

        Booking.objects.create(firstname=firstname, lastname=lastname, mobileno=mobileno, status="Not Updated Yet", email=email, bookingnumber=bookingnumber, address=address, requirementnumber=requirementnumber, shift=shift, gender=gender)
        messages.success(request, "Booking Generated and Booking Number is " + str(bookingnumber))
        return redirect('hiring_form')
    return render(request, "hiring_form.html", locals())

def bookinglist(request):
    action = request.GET.get('action')
    if action == "New":
        data = Booking.objects.filter(status='Not Updated Yet')
    elif action == "Rejected":
        data = Booking.objects.filter(status='Rejected')
    elif action == "Accepted":
        data = Booking.objects.filter(status='Accepted')
    elif action == "All":
        data = Booking.objects.filter()
    return render(request, "new_booking.html", locals())

def request_status(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Booking.objects.filter(Q(bookingnumber__icontains=fromdate))
    return render(request, "request_status.html", locals())

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Admin Login Successful")
                return redirect('dashboard')
            else:
                messages.success(request, "Invalid User")
                return redirect('admin_login')
    return render(request, "admin_login.html")

@login_required(login_url='/admin_login/')
def dashboard(request):
    guard = Guard.objects.filter()
    New = Booking.objects.filter(status="Not Updated Yet")
    Accepted = Booking.objects.filter(status="Accepted")
    Rejected = Booking.objects.filter(status="Rejected")
    All = Booking.objects.filter()
    return render(request, "dashboard.html", locals())

@login_required(login_url='/admin_login/')
def logout_admin(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('admin_login')

@login_required(login_url='/admin_login/')
def add_security_guard(request):
    if request.method == "POST":
        guardname = request.POST['guardname']
        mobilenumber = request.POST['mobilenumber']
        address = request.POST['address']
        idtype = request.POST['idtype']
        idnumber = request.POST['idnumber']
        pic = request.FILES.get('pic')

        Guard.objects.create(guardname=guardname, mobilenumber=mobilenumber, address=address, idtype=idtype, idnumber=idnumber, pic=pic)
        messages.success(request, "Add Successful")
        return redirect('add_security_guard')
    return render(request, "add_security_guard.html", locals())

@login_required(login_url='/admin_login/')
def manage_security_guard(request):
    data = Guard.objects.all()
    d = {'data': data}
    return render(request, "manage_security_guard.html", locals())

@login_required(login_url='/admin_login/')
def edit_security_guard(request, pid):
    if request.method == "POST":
        guardname = request.POST['guardname']
        mobilenumber = request.POST['mobilenumber']
        address = request.POST['address']
        idtype = request.POST['idtype']
        idnumber = request.POST['idnumber']
        try:
            pic = request.FILES['pic']
            c = Guard.objects.get(id=pid)
            c.pic = pic
            c.save()
        except:
            pass

        Guard.objects.filter(id=pid).update(guardname=guardname, mobilenumber=mobilenumber, address=address, idtype=idtype, idnumber=idnumber)
        messages.success(request, "Updated Successful")
        return redirect('manage_security_guard')
    data = Guard.objects.get(id=pid)
    return render(request, "edit_security_guard.html", locals())

@login_required(login_url='/admin_login/')
def change_password(request):
    # user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password')

    return render(request, 'change_password.html')

@login_required(login_url='/admin_login/')
def admin_profile(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        email = request.POST['email']
        uname = request.POST['username']

        user = User.objects.filter(id=request.user.id).update(first_name=fname, email=email, username=uname)
        messages.success(request, "Updation Successful")
        return redirect('admin_profile')
    return render(request, "admin_profile.html", locals())

@login_required(login_url='/admin_login/')
def delete_booking(request, pid):
    data = Booking.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("bookinglist")

@login_required(login_url='/admin_login/')
def delete_security_guard(request, pid):
    data = Guard.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_security_guard")

@login_required(login_url='/admin_login/')
def booking_detail(request, pid):
    data = Booking.objects.get(id=pid)
    if request.method == "POST":
        remark = request.POST['remark']
        status = request.POST['status']
        guardname = request.POST['guardname']
        guardobj = Guard.objects.get(id=guardname)
        data.status = status
        data.save()
        Trackinghistory.objects.create(guardname=guardobj, booking=data, remark=remark, status=status)
        messages.success(request, "Action Updated")
        return redirect('booking_detail', pid)
    traking = Trackinghistory.objects.filter(booking=data)
    myguard = Guard.objects.all()
    return render(request, "booking_detail.html", locals())

def detail_booking(request, pid):
    data = Booking.objects.get(id=pid)
    if request.method == "POST":
        remark = request.POST['remark']
        status = request.POST['status']
        guardname = request.POST['guardname']
        guardobj = Guard.objects.get(id=guardname)
        data.status = status
        data.save()
        Trackinghistory.objects.create(guardname=guardobj, booking=data, remark=remark, status=status)
        messages.success(request, "Action Updated")
        return redirect('booking_detail', pid)
    traking = Trackinghistory.objects.filter(booking=data)
    myguard = Guard.objects.all()
    return render(request, "detail_booking.html", locals())

@login_required(login_url='/admin_login/')
def report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']

        data = Booking.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate)
        data2 = True
    return render(request, "report.html", locals())

@login_required(login_url='/admin_login/')
def search_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        data2 = True
        data = Booking.objects.filter(Q(bookingnumber__icontains=fromdate)|Q(firstname__icontains=fromdate)|Q(lastname__icontains=fromdate)|Q(mobileno__icontains=fromdate))
    return render(request, "search_report.html", locals())












