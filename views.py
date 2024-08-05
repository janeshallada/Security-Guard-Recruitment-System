from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from random import randint
from django.contrib.auth.decorators import login_required
from securityapp.models import*
from securityapp.form import*
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method=="POST":
        uname=request.POST['full_name']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['confirm_password']
        print(uname,email,pass1,pass2)
        if pass1==pass2:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,"u are registered successfully")
            return render(request,'security_form.html',{'username':uname})
        else:
            return HttpResponse("your password and confirm password are not same")
    return render(request,"signup.html")

def Login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=uname,password=pwd)
        print(uname,pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfull")
            data=Guards.objects.get(user1=uname)
            traking=Trackinghistory.objects.filter(guard=data)
            return render(request,'guard_profile.html',{'data':data,'traking':traking})
        else:
            messages.success(request,"invalid credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def guard_profile(request):
    return render(request,"guard_profile.html")


def security_form(request):
    if request.method=="POST":
        form=Guard_form(data=request.POST,files=request.FILES)
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        user1=request.POST['username']
        if form.is_valid():
            u=form.save(commit=False)
            u.user1=user1
            u.guardname=fname+" "+lname
            u.save()
            messages.success(request,"Request Form submitted Successfully")
            return redirect('home')
    else:
        form=Guard_form()
        return render(request,"security_form.html")
    return render(request,"security_form.html")


def admin_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		user= authenticate(username=username,password=password)

		if user:
			if user.is_staff:
				login(request,user)
				messages.success(request,"Admin Login Successful")
				return render(request,"admin_index.html")
			else:
				messages.success(request,"Invalid credentials")
				return render(request,"login.html")

	return render(request,'login.html')

@login_required
def logout_admin(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')

def admin_index(request):
    return render(request,"admin_index.html")

@login_required
def total_applications(request):
	data=Guards.objects.filter(status="Not Updated Yet")
	return render(request,"total_applications.html",{'data':data})


@login_required
def bookingdetails(request,pid):
    data=Guards.objects.get(id=pid)
    if request.method=="POST":
        remark=request.POST['remark']
        status=request.POST['status']
        data.status=status 
        data.save()
        if data.status=="Accepted":
            workplace=request.POST['workplace']
            stime=request.POST['stime']
            etime=request.POST['etime']
            fdate=request.POST['fromdate']
            tdate=request.POST['todate']
            Trackinghistory.objects.create(guard=data,remark=remark,status=status,workplace=workplace,fromtime=stime,totime=etime,fromdate=fdate,todate=tdate)
        else:
            Trackinghistory.objects.create(guard=data,remark=remark,status=status)
        send_mail(
        'Response From ---',
        f" your request is {data.status} please login to Know the details",
        'harikrishnaburada11@gmail.com',
        [data.email],
        fail_silently=False,)
        messages.success(request,"action updated")
        return redirect('total_applications')
    traking=Trackinghistory.objects.filter(guard=data)
    return render(request,"bookingdetails.html",{'data':data,'traking':traking})
@login_required
def work_details(request,pid):
    data=Guards.objects.get(id=pid)
    if request.method=="POST":
        workplace=request.POST['workplace']
        stime=request.POST['stime']
        etime=request.POST['etime']
        fdate=request.POST['fromdate']
        tdate=request.POST['todate'] 
        g=Trackinghistory.objects.get(guard_id=data.id)
        g.workplace=workplace
        g.fromtime=stime
        g.totime=etime
        g.fromdate=fdate
        g.todate=tdate
        g.save()
        messages.success(request,"action updated")
        return redirect('total_guards')
    gd=Trackinghistory.objects.get(guard_id=data.id)
    return render(request,"work_details.html",{'g':gd})


@login_required
def accepted_applications(request):
	data=Guards.objects.filter(status="Accepted")
	return render(request,"accepted_applications.html",{'data':data})

@login_required
def rejected_applications(request):
	data=Guards.objects.filter(status="Rejected")
	return render(request,"rejected_applications.html",{'data':data})
@login_required
def total_guards(request):
	data=Guards.objects.filter(status="Accepted")
	return render(request,"total_guards.html",{'data':data})

@login_required
def delete_guard(request, pid):
	data = Guards.objects.get(id=pid)
	data.delete()
	messages.success(request, "Delete Successful")
	return redirect("total_applications")

@login_required
def profile_update(request):
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        user = User.objects.filter(id=request.user.id).update(username=uname,email=email)
        messages.success(request, "Updation Successful")
        return redirect('admin_index')
    return render(request, "profile_update.html")

@login_required
def change_password(request):
    # user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('admin_index')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password')

    return render(request, 'change_password.html')

@login_required
def profile_update2(request,pid):
    guarddt=Guards.objects.get(id=pid)
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        user = User.objects.filter(id=request.user.id).update(username=uname,email=email)
        user = Guards.objects.filter(user1=guarddt.user1).update(user1=uname)
        data=Guards.objects.get(user1=uname)
        traking=Trackinghistory.objects.filter(guard=data)
        messages.success(request, "Updation Successful")
        return render(request,'guard_profile.html',{'data':data,'traking':traking})
    return render(request, "profile_update2.html")

@login_required
def change_password2(request,pid):
    data=Guards.objects.get(id=pid)
    traking=Trackinghistory.objects.filter(guard=data)
    # user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return render(request,"guard_profile.html",{'data':data,'traking':traking})
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password2')

    return render(request, 'change_password2.html')

@login_required
def training_details(request,pid):
    data=Guards.objects.get(id=pid)
    if request.method=="POST":
        if data.level=="not get any training Level":
            ts=request.POST['status']
            if ts=="Accepted":
                tl=request.POST['address']
                st=request.POST['stime']
                et=request.POST['etime']
                sd=request.POST['sdate']
                ed=request.POST['edate']
                data.level=data.rlevel
                data.save()
                Training.objects.create(guard2=data, tstatus=ts, location=tl, fromtime=st, totime=et, fromdate=sd, todate=ed)
                messages.success(request,"Training details Updated Successfully")
            else:
                Training.objects.create(guard2=data,tstatus=ts)
            return redirect('total_guards')
        else:
            data2=Training.objects.get(guard2_id=data.id) 
            data2.tstatus=request.POST['status']
            data2.location=request.POST['address']
            data2.fromtime=request.POST['stime']
            data2.totime=request.POST['etime']
            data2.fromdate=request.POST['sdate']
            data2.todate=request.POST['edate']
            data2.save()
            data.level=data.rlevel
            data.save()
            messages.success(request,"Traininng details Updated Successfully")
            return redirect('total_guards')
        #     t.guard2=data
        #     t.save()
        #     if t.status=="Accepted":
        #         data.level=data.rlevel
        #     messages.sutccess(request,"Traininng details Updated Successfully")
        #     return redirect('total_guards')
        # else:
        #     form=Train_form()
    return render(request,"training_details.html",{'data':data})

        

def training_level(request,pid):
    data=Guards.objects.get(id=pid)
    data2=None
    if data.level!="not get any training Level":
        data2=Training.objects.get(guard2_id=data.id)
    if request.method=="POST":
        levels=request.POST['level']
        data.rlevel=levels 
        data.save()
        traking=Trackinghistory.objects.filter(guard=data)
        messages.success(request,"Traininng  Level Request submitted Successfully")
        return render(request,"guard_profile.html",{'data':data,'traking':traking})
    return render(request,"training_level.html",{'data':data,'data2':data2})


def issues(request,pid):
    data=Guards.objects.get(id=pid)
    if request.method=="POST":
        data.issue=request.POST['query']
        data.save()
        traking=Trackinghistory.objects.filter(guard=data)
        messages.success(request,"Issue submitted Successfully")
        return render(request,"guard_profile.html",{'data':data,'traking':traking})
    return render(request,'issues.html')



