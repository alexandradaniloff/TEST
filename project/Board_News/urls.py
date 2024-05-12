from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostCreate, PostDetail, PostDelete, PostUpdate, CommentCreate


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('comment/create/', CommentCreate.as_view(), name='comment_create'),



]