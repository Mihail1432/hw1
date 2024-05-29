from django.contrib import admin
from django.urls import path, re_path
from myproject import views  # Імпорт ваших переглядів з вашого додатку

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.article_year, name='article_year'), # URL для головної сторінки

    # Додаткові URL-шляхи
]
