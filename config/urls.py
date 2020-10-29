from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ここでadminやincludeを使うから上でimportしておく
    path('admin/', admin.site.urls),
    # URLの部分、道筋PLOT
    # myapp.urlsは「myappディレクトリのurls.pyに詳しく書いてあるよ」という意味。
    path('myapp1201/', include('myapp1201.urls')),
]
