from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bookshelf(request):
    print("BOOKSHELF REQUEST: ", request)
    user = request.user
    profile = user.profile
    bookshelf = profile.bookshelf
    bookshelfserializer = BookshelfSerializer(bookshelf, many=False)
    return Response(bookshelfserializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    print("BOOKSHELF REQUEST: ", request)
    user = request.user
    profile = user.profile
    bookshelf = profile.bookshelf
    books = bookshelf.books
    booksserializer = BookSerializer(books, many=True)
    return Response(booksserializer.data)


@api_view(['POST'])
@permission_classes([])
def create_user(request):
  user = User.objects.create(
    username = request.data['username'],
  )
  user.set_password(request.data['password'])
  user.save()
  profile = Profile.objects.create(
    user = user,
    first_name = request.data['first_name'],
    last_name = request.data['last_name']
  )
  profile.save()
  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([])
def create_book(request):
    book = Book.objects.create(
        author = request.data['author'],
        genre = request.data['genre'],
        title = request.data['title'],
    )
    book.save()
    book_serialized = BookSerializer(book)
    return Response(book_serialized.data)