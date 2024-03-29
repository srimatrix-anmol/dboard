from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:board_id>',views.board_topics, name='board_topics'),
    path('<int:board_id>/new', views.new_topic, name='new_topic'),
]
