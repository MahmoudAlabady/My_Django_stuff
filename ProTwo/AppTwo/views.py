from django.shortcuts import render
##from django.http import HttpResponse
##from AppTwo.models import User
from AppTwo.forms import NewUserForm
# def index(request):
#     return HttpResponse('<em>My Second App</em>')
# Create your views here.
def index(request):
    my_dict = {"Help_Tap":"THis is view for help tag"}
    return render(request,'second_app/index.html')


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')
    return render(request,'second_app/users.html',{'form':form})          

















    # user_list = User.objects.order_by('First_Name')
    # user_dict = {'users': user_list}
    #
    # return render(request, 'second_app/users.html', context=user_dict)
