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

