from django.contrib import admin
from movies.models import (FilmWork, Genre, GenreFilmWork, Person,
                           PersonFilmWork)


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)
    list_display = (
        "id",
        "title",
        "type",
        "creation_date",
        "rating",
        "created",
        "modified",
    )
    list_filter = ("type",)
    search_fields = ("title", "description", "id")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "created",
        "modified",
    )
    search_fields = ("id", "full_name", "created", "modified")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created",
        "modified",
    )
    search_fields = ("id", "name", "created", "modified")
