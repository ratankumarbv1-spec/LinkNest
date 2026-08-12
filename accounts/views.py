from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:

        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('dashboard')

    else:

        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):

    logout(request)

    return redirect('landing')

@login_required
def profile(request):

    user = request.user

    links = user.links.all()

    favourite_count = links.filter(
        is_favourite=True
    ).count()

    category_count = (
        links
        .values('category')
        .distinct()
        .count()
    )

    return render(
        request,
        'profile.html',
        {
            'user': user,
            'link_count': links.count(),
            'favourite_count': favourite_count,
            'category_count': category_count,
        }
    )