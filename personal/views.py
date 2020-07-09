from django.shortcuts import render
from accounts.models import Account

# Create your views here.


def home_screen_view(request):
    # print(request.headers)
    context = {}
    '''context['some_string'] = "passing varible in django"
    context['mobile'] = "99580224324"
    list_of_values = []
    list_of_values.append("check1")
    list_of_values.append("check2")
    list_of_values.append("check3")
    context['list_of_values'] = list_of_values
    questions = Question.objects.all()
    context['questions'] = questions'''
    users = Account.objects.all()
    context['users'] = users

    return render(request, "personal/home.html", context)
