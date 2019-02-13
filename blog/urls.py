from django.urls import path
from blog.views import hello_times
from blog.views import index, hello_times
from blog.views import articles_by_year

from django.urls import register_converter
from blog.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'year')

app_nmae = 'blog'  

urlpatterns = [
    path('articles/<year:year>/', articles_by_year),

    # re_path('^blog/1/$', post_detail),
    # re_path('^blog/1/edit/$', post_edit),

    path('', index),
    # re_path(r'^$', index),
    path('blog/hello_times/<int:times>', hello_times),
    path('', index),
]
