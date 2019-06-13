from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from .forms  import NewTopicForm
# Create your views here.


def home(request):
    board = Board.objects.all()
    return render(request, 'home.html', {'boards': board})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()  # ToDo: get the current logged on user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic= form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', board_id=board.pk) #ToDo
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})