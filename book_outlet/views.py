from django.shortcuts import render
from . models import Book
# Create your views here.

def index(request):
    book=Book.objects.all().order_by("-title")
    return render(request,"book_outlet\index.html",{
        "books":book
        })
# def book_detail(request,id):
#     Book_details=Book.objects.get(pk=id)
def book_detail(request,slug):
    Book_details=Book.objects.get(slug=slug)
    return render(request,"book_outlet/details.html",{
        "title":Book_details.title,
        "author":Book_details.author,
        "rating":Book_details.rating,
        "is_bestselling":Book_details.is_bestselling
        })