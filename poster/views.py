from django.contrib import messages
from django.contrib.auth import logout, login
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import CreateView

from .forms import *
from .models import *

menu = [{'title': 'Афиша', 'url_name': 'afisha'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Отзывы', 'url_name': 'review'},
        {'title': 'О нас', 'url_name': 'dj_cinema'},
        ]


# Расширение меню навигации
def menu_extend(request):
    if request.user.is_authenticated:
        while True:
            try:
                menu.remove({'title': 'Вход', 'url_name': 'login'})
                menu.remove({'title': 'Регистрация', 'url_name': 'registration'})
            except ValueError:
                try:
                    menu.remove({'title': 'Выход', 'url_name': 'site_logout'})
                except ValueError:
                    break
        menu.append({'title': 'Выход', 'url_name': 'site_logout'})
    else:
        while True:
            try:
                menu.remove({'title': 'Выход', 'url_name': 'site_logout'})
            except ValueError:
                try:
                    menu.remove({'title': 'Вход', 'url_name': 'login'})
                    menu.remove({'title': 'Регистрация', 'url_name': 'registration'})
                except ValueError:
                    break
        menu.extend([{'title': 'Вход', 'url_name': 'login'},
                     {'title': 'Регистрация', 'url_name': 'registration'},
                     ])


# Страничка приветствия
def welcome(request):
    menu_extend(request)
    return render(request, 'poster/main.html', {'menu': menu, })


# Страничка с контактами кинотеатра
def about_cinema(request):
    cinemas = Cinema.objects.all()
    menu_extend(request)
    context = {'cinemas': cinemas,
               'menu': menu,
               }
    return render(request, 'poster/djabout.html', context=context)


# Афиша кинотеатра
def afisha(request):
    films = Film.objects.all()
    title = "Сейчас в кино"
    menu_extend(request)
    context = {'films': films,
               'menu': menu,
               'title': title,
               }
    return render(request, 'poster/afisha.html', context=context)


# Фильм и сеансы
def about_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    sessions = Session.objects.filter(film_id=film_id)
    menu_extend(request)
    context = {
        'film': film,
        'sessions': sessions,
        'menu': menu,
        'title': film.name,
    }
    return render(request, 'poster/filmabout.html', context=context)


# Новости кинотеатра
def news(request):
    djnews = News.objects.all()
    title = "Новости DJ-Cinema"
    menu_extend(request)
    context = {'news': djnews,
               'menu': menu,
               'title': title,
               }
    return render(request, 'poster/news.html', context=context)


# Читать подробнее о новости
def about_new(request, new_id):
    new = get_object_or_404(News, pk=new_id)
    menu_extend(request)
    context = {
        'new': new,
        'menu': menu,
        'title': new.title,
    }
    return render(request, 'poster/newabout.html', context=context)


# Отзывы о кинотеатре
def review(request):
    djreviews = Review.objects.all()
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.author_id = request.user
            rev.save()
            return redirect('review')
        else:
            messages.error(request, "Ooops, something goes wrong:(")
    else:
        form = AddReviewForm()
    menu_extend(request)
    context = {
        'reviews': djreviews,
        'menu': menu,
        'user_logged_in': request.user.is_authenticated,
        'form': form,
    }
    return render(request, 'poster/review.html', context=context)


# Страничка при ошибке 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Регистрация
def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            us1 = form.save()
            login(request, us1)
            messages.success(request, "Now you're a part of our cinema!")
            return redirect('login')
        else:

            messages.error(request, "Ooops, something goes wrong:(")
    else:
        form = RegisterForm()
    context = {"form": form,
               'menu': menu}
    return render(request, "poster/registration.html", context=context)


# Вход
def site_login(request):
    if request.method == "POST":
        form = SiteLogForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = SiteLogForm()
    context = {"form": form,
               'menu': menu}
    return render(request, "poster/site_login.html", context=context)


# Выход
def site_logout(request):
    logout(request)
    return redirect('welcome')
