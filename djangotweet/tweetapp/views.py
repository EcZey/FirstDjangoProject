from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dict={'tweets':all_tweets}
    return render(request,"tweetapp/listtweet.html",context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        nickname= request.POST["nickname"]
        message= request.POST["message"]
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))

    return render(request,"tweetapp/addtweet.html")


class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"