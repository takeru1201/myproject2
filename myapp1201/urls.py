from django.urls import path
# 同じ階層のviews.pyと紐付け
from . import views

# myapp1201のURLを指定する場所
app_name = 'myapp1201'
urlpatterns = [
    # views.pyに定義されているIndexViewに定義されているIndexView関数として使用
    path('', views.IndexView.as_view(), name='index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    # viewsの後はクラス名views.pyで定義する
    path('register/director/', views.RegisterDirectorView.as_view(), name='movie_diteil'),
    path('redister/movie/', views.RegisterMovieView.as_view(), name='registermovie'),
    path('writing/log', Views.WritingLogView.as_view(), name='writinglog'),
]