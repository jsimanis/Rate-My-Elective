import json, urllib
from mysite.settings import GOOGLE_RECAPTCHA_SECRET_KEY
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from website.forms import UserLoginForm, UserRegisterForm, ContactForm, AddClassForm, ReviewForm, AddDeptForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from website.models import Course, Review, Department
from django.contrib.auth.models import User
from django.db.models import Q


def home(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        objs = Course.objects.filter(
            (Q(course_number__icontains=query) and Q(
                department__code__icontains=query))
            | Q(name__icontains=query)
            | Q(course_number__icontains=query)
            | Q(department__code__icontains=query))
        if len(objs)==0:
            objs = Course.objects.all()
            return render(request, "home.html", {'other_classes': objs})

        return render(request, "home.html", {'objs': objs})
    else:
        return render(request, "home.html", {'no_query':True})
    


def elective(request, department, classNum):
    current_user = request.user

    url = "/elective/" + str(department) + "/" + str(classNum)
    
    if current_user.is_authenticated:
        elective_obj = Course.objects.get(course_number=classNum, department=department)
        reviews_obj = Review.objects.filter(Q(course__exact=elective_obj))
        if request.method=='POST' and 'create-review-button' in request.POST:
           
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.instance.course= elective_obj
                form.instance.author=User.objects.get(id=current_user.id)
                form.save()
                form = ReviewForm()
                return HttpResponseRedirect(url)
        elif request.method=='POST':
            pass
        else:
          
          form = ReviewForm()
        context = {
            "elective": elective_obj,
            "reviews": reviews_obj,
            'form': form
        }        
        return render(request, "elective.html", context=context)
    else:
        return redirect(loginUser)


def edit_review(request, review):
    current_user = request.user


#def edit_review(request, )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contactconfirm)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contactconfirm(request):
    return render(
        request,
        'contact_confirm.html',
    )


def addClass(request):
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contactconfirm)
    else:
        form = AddClassForm()
    return render(request, 'add_class.html', {'form': form})

def addDept(request):
    if request.method == 'POST':
        form = AddDeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contactconfirm)
    else:
        form = AddDeptForm()
    return render(request, 'add_dept.html', {'form': form})


def search(request):
    #objs = Course.objects.all()
    objs = Course.objects.filter(
        Q(name__icontains="326")
        | Q(course_number__icontains="326"))  #search results

    #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#id4
    return render(request, "search_results.html", {'objs': objs})


def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            redirect(registerUser)
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form': form})


def loginUser(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(home)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect(home)


#def deleteUser(request):


def profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        objs = Review.objects.filter(author__username=request.user.username)

        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, "profile.html", {'form': form, 'objs' : objs})
          #return render(request, "profile.html")

    else:
        return redirect(loginUser)


def delete_account(request):
    context = {}
    try:
        request.user.is_active = False
        request.user.save()
        context['msg'] = 'Profile successfully disabled.'
        return redirect(loginUser)
    except Exception as e:
        context['msg'] = e
    return redirect(loginUser)

def delete_review(request, review):
  print(request)
  print(review)


def flag_review(request):
    context = {}

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, '/profile', {
        'form': form
    })


def flag_review(request):
    context = {}


def rate_review_positive(request, review):
  current_user = request.user
  if current_user.is_authenticated:
    if request.method == 'POST':
      review.rating_positive += 1
  else:
    return redirect(loginUser)

def rate_review_negative(request, review):
  current_user = request.user
  if current_user.is_authenticated:
    if request.method == 'POST':
      review.rating_positive -= 1
  else:
    return redirect(loginUser)

def flag_review(request, review):
    if review.flagged == True:
      review.flagged = False
    else:
      review.flagged = True
    