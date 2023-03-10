from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            books = books.filter(title__icontains=title)
        
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try: 
        book = Book.objects.get(pk=pk) 
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        book_serializer = BookSerializer(book) 
        return JsonResponse(book_serializer.data) 
 
    elif request.method == 'PUT': 
        book_data = JSONParser().parse(request) 
        book_serializer = BookSerializer(book, data=book_data) 
        if book_serializer.is_valid(): 
            book_serializer.save() 
            return JsonResponse(book_serializer.data) 
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        book.delete() 
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def book_list_publisher(request, publisher):
    books = Book.objects.filter(publisher=publisher)
        
    if request.method == 'GET': 
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    