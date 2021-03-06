from django.urls import path
# 同じ階層のviews.pyと紐付け
from . import views

# myapp1201のURLを指定する場所
app_name = 'myapp1201'
urlpatterns = [
    # views.pyに定義されているIndexViewに定義されているIndexView関数として使用
    path('', views.IndexView.as_view(), name='index'),
    # views.pyではMovieDetailView関数として定義、でもうrlで使うときはmovie_detail
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    # viewsの後はクラス名views.pyで定義する
    path('register/director/', views.RegisterDirectorView.as_view(), name='registerdirector'), #これ追加
    path('register/movie/', views.RegisterMovieView.as_view(), name='registermovie'), #これ追加
    path('writing/log/', views.WritingLogView.as_view(), name='writinglog'), #これ追加
]