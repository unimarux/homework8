from django.shortcuts import render , get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Type,Flower

# categoryes = Type.objects.all()
books = Flower.objects.all()

context = {
    # "categoryes":categoryes,
    "books":books,
    "title":'Barcha Gullar'
}
def main(request :WSGIRequest):
    return render(request,'index.html',context)

def books_by_category(request :WSGIRequest,category_id):
    # categoryes_2 = Type.objects.all()
    books_2 = Flower.objects.filter(category_id=category_id)
    context_for_books_in_category ={
        # "categoryes":categoryes_2,
        "books":books_2,
        "title":f"{Type.name} : Flowers"

    }
    return render(request,'index.html',context_for_books_in_category)


def book_detail(request:WSGIRequest,pk):
    book_3 = get_object_or_404(Flower , pk=pk)
    context = {
        "book":book_3,
        "title":Flower.title
    }
    return render(request,'Detail.html',context)

def about_us(request :WSGIRequest):
    return render(request,'about_us.html',context)

def contact(request: WSGIRequest):
    return render(request,'contacts.html',context)

