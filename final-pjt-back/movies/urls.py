from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/comments/', views.moviecomment_create),
    path('comments/<int:comment_pk>/', views.moviecomment_delete),
    path('title/', views.movie_title),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('reviews/comments/<int:comments_pk>/', views.comment_delete),

]