from rest_framework import serializers
from .models import Movie, Review, ReviewComment, MovieComment, Genre
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class MovieListSerilizer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreSerializer(read_only=True, many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieListSerilizer(read_only=True)

    class Meta:
        model = MovieComment
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    moviecomment_set = MovieCommentSerializer(many=True, read_only=True)
    
    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    class ReviewListSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)
        class Meta:
            model = Review
            fields = ('pk','user', 'title', 'content',)

    review_set = ReviewListSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField(
        source='review_set.count', read_only=True
    )
    genres = GenreSerializer(read_only=True, many=True)
    like_users = LikeUserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(
        source='like_users.count', read_only=True
    )

    class Meta:
        model = Movie
        fields = '__all__'

class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title',)

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
    user = UserSerializer(read_only=True)
    review = ReviewListSerializer(read_only=True)
    class Meta:
        model = ReviewComment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
    user = UserSerializer(read_only=True)
    
    reviewcomment_set = CommentSerializer(many=True, read_only=True)

    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'