from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Board, Topic, Post
# Create your views here.


def home(request):
    board = Board.objects.all()
    return render(request, 'home.html', {'boards': board})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first() # ToDo: get the current logged on user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', board_id=board.pk) #ToDo

    return render(request, 'new_topic.html', {'board': board})