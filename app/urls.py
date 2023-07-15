from django.urls import path
from app.views import index_view, all_blogs, article, contact_view


urlpatterns = [
    path('', index_view, name='index'),
    path('all_blogs', all_blogs, name='all_blogs'),
    path('article/<int:blog_id>', article, name='article'),
    path('contact/', contact_view, name='contact')
]