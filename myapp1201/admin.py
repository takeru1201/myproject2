from django.contrib import admin
# models.pyで作った表を再利用
from myapp1201.models import Director, Movie, Log

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Log)




# Register your models here.
