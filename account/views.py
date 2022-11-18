from django.shortcuts import redirect, render
from django.contrib.auth import login

from .forms import CreateReviewUserForm


def register_view(request):

    form = {}
    if request.method == "POST":
        form = CreateReviewUserForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            login(request, user.user)
            return redirect("item:home")
        else:
            pass
    else:
        form = CreateReviewUserForm()

    context = {"form": form}
    return render(request, "account/register.html", context)
