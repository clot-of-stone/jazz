from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
from .converters import DateConverter


def books_detail(request, pub_date):
    dates = [DateConverter().to_url(book['pub_date']) for book in
             Book.objects.order_by('pub_date').values('pub_date').distinct()]
    paginator = Paginator(dates, 1)
    count = dates.index(DateConverter().to_url(pub_date))
    page = paginator.get_page(count + 1)
    if page.has_next():
        next_date = dates[count + 1]
    else:
        next_date = None
    if page.has_previous():
        previous_date = dates[count - 1]
    else:
        previous_date = None
    books = Book.objects.filter(pub_date=pub_date)
    context = {
        'next_date': next_date,
        'previous_date': previous_date,
        'page': page,
        'books': books,
    }
    template = 'books/books_list.html'

    return render(request, template, context)


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all().order_by('-pub_date')}
    return render(request, template, context)
