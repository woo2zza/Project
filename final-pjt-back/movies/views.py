from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status



from .models import Movie, Genre, Review, MovieComment, ReviewComment
from .serializers import MovieListSerilizer, MovieSerializer, ReviewSerializer, ReviewListSerializer, CommentSerializer, MovieTitleSerializer, MovieCommentSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerilizer(movies, many=True)
        return Response(serializer.data)




@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    
@api_view(['GET'])
def movie_title(request):
    titles = get_list_or_404(Movie)
    serializer = MovieTitleSerializer(titles, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        movie_pk = request.data.get('movie')
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)

@api_view(['GET', 'DELETE','PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        movie_pk = request.data.get('movie')
        movie = get_object_or_404(Movie, pk=movie_pk)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data)

@api_view(['POST', 'GET'])
def comment_create(request, review_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user = request.user)
            return Response(serializer.data)

        

@api_view(['DELETE'])
def comment_delete(request, comments_pk):
    comment = get_object_or_404(ReviewComment, pk=comments_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST', 'GET'])
def moviecomment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def moviecomment_delete(request, comment_pk):
   comment = get_object_or_404(MovieComment, pk=comment_pk)
   comment.delete()
   return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['POST'])
def like_movie(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
