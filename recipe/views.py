from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Recipe


def last_views(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]
    my_context={'recipes': recipes}
    return render(request, 'main.html', my_context)


def all_categories(request):
    categories = Category.objects.all()

    counts = []
    for category in categories:
        counts.append({
            'name_of_category': category.name,
            'count_of_every': category.categories.count()
        })
    return render(request, 'new.html', {'counts': counts})