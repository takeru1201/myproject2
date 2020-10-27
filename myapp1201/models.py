# 表を作るためのモジュールを再利用
from django.db import models
# 時間を扱うためのモジュールを再利用
from django.utils import timezone

# modelsを使いDirectorという表を作る
class Director(models.Model):
  name = models.CharField(max_length=100, verbose_name="監督")
  # 文字列を表示するための特殊メソッド
  def __str__(self):
      return self.name

class Movie(models.Model):
  title = models.CharField(max_length=100, verbose_name="タイトル")
  # timezoneというモジュールを上で定義したので日付を入力できる
  watch_date = models.DateField()
  # directorはDirectorという表から情報を参照しますという宣言
  director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="監督", related_name="movie")
  def __str__(self):
      return self.title

class Log(models.Model):
  text = models.TextField()
  # movieはMovieという表から参照しますよという宣言
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="タイトル", related_name='log')
  def __str__(self):
      return self.text

  



# Create your models here.
