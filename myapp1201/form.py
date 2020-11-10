# form.pyはHTMLで入力したものをmodelに渡す為のファイル
from django.forms import ModelForm
from myapp1201.models import Movie, Director, Log

class DirectorForm(ModelForm):
    # どのデータを使うか。どの項目を使うか。
    class Meta:
        model = Director
        fields = ('name',)

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'watch_date', 'director')

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('movie', 'text')