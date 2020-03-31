from django.db import models
import uuid
from django import urls
from django.urls import reverse


class author(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField('death', null=True, blank=True)

    def __str__(self):
        return ' %s %s ' % (self.firstname, self.lastname)

    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])


class genre(models.Model):
    genre = models.CharField(max_length=200, help_text='genre')

    def __str__(self):
        return self.genre


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='enter describtion')
    isbn = models.CharField('isbn', max_length=13, help_text='13 character')
    genre = models.ManyToManyField(genre, help_text='select genre')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details', args=[str(self.id)])

    def display_genre(self):
        return ' , '.join(genre.genre for genre in self.genre.all()[:3])

    def display_auther(self):
        return ' %s ' %(self.author.firstname)

    display_genre.short_description = 'genre'


class BookInstanse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for this')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=300)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'maintenance'),
        ('o', 'onload'),
        ('a', 'availble'),
        ('r', 'reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='book availble')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return ' %s , %s ' % (self.id, self.book.title)
