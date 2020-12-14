from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,'login_page.html')

def ticket(request):
        if request.method == 'POST':

                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print('user created')
                return render(request,'new_ticket_page.html')

def submit_ticket(request):
        return redirect('api/ticket_table/')