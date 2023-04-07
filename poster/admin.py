from django.contrib import admin

from .models import *


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'year', 'production']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'genre', 'year', 'production']


class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'data_time']
    list_display_links = ['id', 'data_time']
    search_fields = ['id', 'data_time']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'price']
    list_display_links = ['id', 'price']
    search_fields = ['id', 'price']


class SeatRowAdmin(admin.ModelAdmin):
    list_display = ['id', 'row', 'place', 'category']
    list_display_links = ['id', 'row', 'place']
    search_fields = ['id', 'row', 'place']


class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district', 'address', 'numbers']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'data']
    list_display_links = ['id', 'author_id']
    search_fields = ['id', 'author_id']


admin.site.register(FilmGenre)
admin.site.register(FilmProduction)
admin.site.register(Film, FilmAdmin)
admin.site.register(SeatCategory)
admin.site.register(Session, SessionAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(SeatRow, SeatRowAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Review, ReviewAdmin)

