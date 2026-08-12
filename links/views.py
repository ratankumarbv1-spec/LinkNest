from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Link


def landing(request):
    return render(request, 'landing.html')


@login_required
def dashboard(request):

    links = Link.objects.filter(
        user=request.user
    )

    # Search
    search_query = request.GET.get(
        'search',
        ''
    )

    if search_query:

        links = links.filter(
            title__icontains=search_query
        ) | links.filter(
            description__icontains=search_query
        )


    # Category
    selected_category = request.GET.get(
        'category',
        ''
    )

    if selected_category:

        links = links.filter(
            category=selected_category
        )


    # Favorites
    if request.GET.get('favourites') == 'true':

        links = links.filter(
            is_favourite=True
        )


    # Statistics
    user_links = Link.objects.filter(
        user=request.user
    )

    favourite_count = user_links.filter(
        is_favourite=True
    ).count()

    category_count = (
        user_links
        .values('category')
        .distinct()
        .count()
    )


    return render(
        request,
        'dashboard.html',
        {
            'links': links,
            'favourite_count': favourite_count,
            'category_count': category_count,
            'search_query': search_query,
            'selected_category': selected_category,
        }
    )



@login_required
def add_link(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        category = request.POST.get('category')
        is_favourite = request.POST.get('is_favourite') == 'on'

        Link.objects.create(
            user=request.user,
            title=title,
            url=url,
            description=description,
            category=category,
            is_favourite=is_favourite
        )

        return redirect('dashboard')

    return render(request, 'add_link.html')

@login_required
def edit_link(request, link_id):

    link = Link.objects.get(
        id=link_id,
        user=request.user
    )

    if request.method == 'POST':

        link.title = request.POST.get('title')

        link.url = request.POST.get('url')

        link.description = request.POST.get(
            'description'
        )

        link.category = request.POST.get(
            'category'
        )

        link.is_favourite = (
            request.POST.get('is_favourite') == 'on'
        )

        link.save()

        return redirect('dashboard')

    return render(
        request,
        'edit_link.html',
        {
            'link': link
        }
    )


@login_required
def delete_link(request, link_id):

    link = Link.objects.get(
        id=link_id,
        user=request.user
    )

    if request.method == 'POST':

        link.delete()

        return redirect('dashboard')

    return render(
        request,
        'delete_link.html',
        {
            'link': link
        }
    )