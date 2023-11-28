from rest_framework import serializers
from django.contrib.auth import get_user_model
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from movies.models import Movie, Review, ReviewComment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'profile_pic')


class ReviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'pk',
            'title',
        )
        
class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title','poster_path')
        
class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class FollowFollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
            
    class MovieSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class LikeUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('id',)

        like_users = LikeUserSerializer(read_only=True, many=True)
        like_user_count = serializers.IntegerField(
            source='like_users.count', read_only=True
        )

        class Meta:
            model = Movie
            fields = '__all__'


    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(
        source='followers.count', read_only=True
    )
    following_count = serializers.IntegerField(
        source='followings.count', read_only=True
    )
    
    class ReviewSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('id', 'username')
        user = UserSerializer(read_only=True)
        movie = MovieTitleSerializer(read_only=True)
        reviewcomment_set = CommentSerializer(many=True, read_only=True)
        commentcount = serializers.IntegerField(source='reviewcomment_set.count', read_only=True)

        class Meta:
            model = Review
            fields = '__all__'

    review_set = ReviewSerializer(many=True)
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')

