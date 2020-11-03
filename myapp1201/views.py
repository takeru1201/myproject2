# views.pyはrailsでいうコントローラー
# 汎用ビューを使用する為のgeneric
from django.views import generic
from myapp1201.models import Movie, Director, Log

# ListViewが汎用ビュー
class IndexView(generic.ListView):
    template_name = 'myapp1201/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'myapp1201/detail.html'

class RegisterDirectorView(generic.CreateView):
  # 格納するデータベースの項目
  model = Director
  # 上の項目を何に使い方
  form_class = DirectorForm
  入力画面を表示するHTMLファイルURL
  template_name = 'myapp1201/register.html'
  # データの入力と格納がうまくできた後の行先
  def get_success_url(self):
    # 行先はmyapp1201/register/movie
    return reverse('myapp1201:registermovie')

class RegisterMovieView(generic.CreateView):
  model = Movie
  form_class = MovieForm
  template_name = 'myapp1201/register.html'
  def get_success_url(self):
    # pkは自動ID紐付けされている。(映画メイト監督と日付)
    return reverse('myapp1201:movie_detail', kwargs={'pk': self.object.pk})