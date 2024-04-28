from django.http import HttpResponse
from django.shortcuts import render,redirect
# from Website import service
from service.models import Services,taskTable
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

@login_required(login_url='login/')
def homePage(request):
    serviceData = Services.objects.all() 
    if search_query := request.GET.get('search', None):
        serviceData = serviceData.filter(service_title__icontains = search_query)      
    data = {
        'serviceData':serviceData
    }
    return render(request,"index.html",data)

def Login(request):
    if request.user.is_authenticated:
        return redirect("/work/")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Inavild Username or  Password!')
            return redirect('login')

        user = authenticate(username = username,password = password)
        if user is None:
            messages.error(request,'Inavild Username or Password')
            return redirect('login')
        else:
            login(request,user)
            return redirect('/work/')
    return render(request,"Login.html")
def Signin(request):
    if request.method == "POST":
        name = request.POST['UserName']
        fname = request.POST['fName']
        lname = request.POST['lName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.filter(username=name)
        if user.exists():
            messages.error(request,'Username is alread taken..!')
            return redirect('signin')
        
        if pass1 != pass2:
            error = "Password doesn't match"
            return render(request, "Sigin.html", {"error": error})
        
        if len(pass1) < 6:
            error = "Password must be at least 6 characters long"
            return render(request, "Signin.html", {"error": error})
        
        user = User.objects.create(
            username = name,
            first_name=fname,
            last_name=lname,
        )

        user.set_password(pass1)
        user.save()
        send_mail(
            f'Hello {fname}',
            'Thank you for registering at our site',
            'djangotest1635@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.info(request,'Your account has been created successfully')
        return redirect('login')


    return render(request,"Signin.html")
def Signup(request):
    return render(request,"Signup.html")
def Signout(request):
    logout(request)
    messages.success(request,"Log out successfully")
    return redirect('/')

@login_required(login_url='login/')
def Work(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # fname = user.first_name
            return redirect("work.html",)
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('work/')
    serviceData = Services.objects.filter(user=request.user)
   
    data = {
        'serviceData':serviceData,
        }
    return render(request,"work.html",data)
@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['phnnumber']
        msg = request.POST['msg']
        send_mail(
            f'Mr/Mrs {name}',
            f'Message is :{msg} & Number : {number}',
            f'{email}',
            ['djangotest1635@gmail.com'],
            fail_silently=False,
        )
    return render(request,"contact.html")
@login_required(login_url='/login/')
def about(request):
    return render(request,"about.html")
@login_required(login_url='/login/')
def form(request):
    if request.method =="POST":
        user=request.user.id
        print("-----------------------------------------------------------",user)
        Icon = request.POST.get('icon')
        title = request.POST.get('sertitle')
        description = request.POST.get('serdes')
        save = Services.objects.create(service_icon = Icon,service_title= title,service_des = description,user_id=user)
            # save.save()
            # k=save.pk
            # print('-----------------------)
            # print("=========================",k)
        
        return redirect('work')
    return  render(request,'form.html')

def table(request, service_id):
    print("====123=====",service_id)

    taskData = taskTable.objects.filter(user=request.user,service=service_id)    
    data = {
        'service_id': service_id,
        'taskData': taskData,
    }
    return render(request, "table.html", data)
@login_required(login_url= "/login/")
def tableForm(request,service_id):
    if request.method == "POST":
        user = request.user.id
        name = request.POST['taskName']
        title = request.POST["taskTitle"]
        description = request.POST["taskDes"]        
        # print("-------------------====================",service_id)
        save = taskTable.objects.create(user_id=user,service_id=service_id,Name = name,Title = title, Description = description)
        print("--------------------",save)
        return redirect(reverse('table', args=[service_id]))
    return render(request,"Tableform.html",{'service_id': service_id})


def Delete(request,service):
    s = taskTable.objects.get(pk=service)
    service_id = s.service_id
    s.delete()
    return redirect(reverse('table', kwargs={'service_id':service_id}))
def SDelete(request,service):
    st = Services.objects.get(pk=service)    
    st.delete()
    return redirect('work')



def Update(request,service):
    std = taskTable.objects.get(pk=service)
    return  render(request,"UpdateTask.html",{'std':std,'service':service})

def Updated_data(request,service):
        user = request.user.id
        name = request.POST['taskName']
        title = request.POST["taskTitle"]
        description = request.POST["taskDes"]        

        std = taskTable.objects.get(pk=service)
        std.Name = name
        std.Title = title
        std.Description = description
        service_id=std.service_id
        std.save()
        return redirect(reverse('table', kwargs={"service_id":service_id}))

