from django.contrib import admin
from . import models



@admin.register(models.author)
class admin_auther(admin.ModelAdmin):
    list_filter = ['firstname']
    list_display = ['firstname','lastname']


class BookInstances(admin.TabularInline):
    model = models.BookInstanse
    extra = 1


@admin.register(models.genre)
class admin_genre(admin.ModelAdmin):
    pass


@admin.register(models.Book)
class admin_book(admin.ModelAdmin):
    list_display = ('title', 'display_auther', 'display_genre')
    list_filter = ('title', 'author')
    inlines = [BookInstances]


@admin.register(models.BookInstanse)
class admin_BookInstance(admin.ModelAdmin):
    fieldsets = (
        ('information: ', {'fields': ('id', 'book', 'imprint')}),
        ('available:', {'fields': ('status', 'due_back')})
    )
