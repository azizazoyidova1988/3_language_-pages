from django.shortcuts import render, redirect
from .models import Post, Follower, Subscribers, Advertising
from .forms import SubscribersForm
from . import services
from django.utils.translation import gettext_lazy as _


def home(request):
    CODE = request.LANGUAGE_CODE
    print(CODE)
    posts = services.get_posts(CODE)
    followers = services.get_followers(CODE)
    advertisings = Advertising.objects.all().order_by('-created_at')[:3]
    model = Subscribers()
    form = SubscribersForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        'posts': posts,
        'followers': followers,
        'advertisings': advertisings,
        "form": form,
        "welcome": _("WELCOME_TEXT"),
        "service1": _(" SERVICE_TEXT_1"),
        "service2": _(" SERVICE_TEXT_2"),
        "service3": _(" SERVICE_TEXT_3"),
    }
    return render(request, 'index.html', ctx)
