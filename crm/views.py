from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from crm.models import Book
from crm.forms import BookModelForm,RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

#decorators
def signin_required(fn):

    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request," failed to login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


# Create your views here.             disp=get work cheyyano post work cheyyanoon theermanikkm
@method_decorator(signin_required,name="dispatch")
class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("entered")
            messages.success(request,"added succesfully")

            return render(request,"book_add.html",{"form":form})

        else:
            print("failed")
            messages.error(request,"failed to add")

            return render(request,"book_add.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")
class BooklistView(View):
    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        if "genre" in request.GET:
            gen=request.GET.get("genre")
            qs=qs.filter(genre=gen)

        return render(request,"book_list.html",{"data":qs})
    
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Book.objects.filter(name_icontains=name)
        return render(request,"book_list.html",{"data":qs})
        
@method_decorator(signin_required,name="dispatch")
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_details.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        form=BookModelForm(instance=qs)
        return render(request,"book_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        form=BookModelForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            messages.success(request,"updated succesfully")

            return redirect("book-list")
        else:
            print("not")
            messages.error(request,"failed to update")
        return render(request,"book_update.html",{"form":form})
    
@method_decorator(signin_required,name="dispatch")
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
       id=kwargs.get("pk")
       Book.objects.get(id=id).delete()
       messages.success(request,"deleted succesfully")
       return redirect("book-list")
    
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"successfully created ")
            print("ok")
            return render(request,"register.html",{"form":form})
        else:
            print("not")
            messages.error(request,"failed to create account")
            return render(request,"register.html",{"form":form})
      


class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(user_name,pwd)
            user_obj=authenticate(request,username=user_name,password=pwd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)#cession start cheyyan
                messages.success(request,"login succesfully")
                return redirect("book-list")
        
        messages.error(request,"failed to login")
        return render(request,"login.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,"logout successfully")
        return redirect("signin")








# class BookDeleteView(View):