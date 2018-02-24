from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.shortcuts import get_object_or_404
from .forms import NewTopicForm, PostForm
from django.db.models import Count

# Create your views here.

def home(request):
	boards = Board.objects.all()
	context = {
		'boards':boards,
	}
	return render(request, 'home.html', context)


def board_topics(request, pk):
	try:
		board = Board.objects.get(pk=pk)
	except:
		raise Http404

	context = {
		'board':board,
	}
	return render(request, 'topics.html', context)

# This is an example for WITHOUT USING FORMS.PY

# def new_topic(request,pk):
# 	board = get_object_or_404(Board, pk=pk)
# 	if request.method=='POST':
# 		subject = request.POST['subject']
# 		message = request.POST['message']

# 		user = User.objects.first() # TODO: get the currently logged user

# 		topic = Topic.objects.create(subject=subject, board=board, starter=user)
# 		post = Post.objects.create(message=message, topics=topic, created_by=user)

# 		return redirect('boards', pk=board.pk)

# 	context = {
# 		'board':board,
# 	}
# 	return render(request,'new_topic.html', context)
# -------------------------------------------------------------------

# USING FORMS.PY
@login_required
def new_topic(request,pk):
	board=get_object_or_404(Board, pk=pk)

	if request.method=='POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board=board
			topic.starter = request.user
			topic.save()
			post=Post.objects.create(message=form.cleaned_data.get('message'), topics=topic, created_by=request.user)
			return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
	else:
		form = NewTopicForm()
	
	context = {
	'board':board,
	'form':form,
	}

	return render(request, 'new_topic.html', context)

def topic_posts(request, pk, topic_pk):
	topic = get_object_or_404(Topic, pk=pk)
	return render(request, 'topic_posts.html', {'topic':topic})

@login_required
def reply_topic(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if request.method=='POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()
			return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
	else:
		form = PostForm()
	
	context = {
	'topic':topic,
	'form':form,
	}

	return render(request, 'new_topic.html', context) 

def board_topics(request, pk):
	board = get_object_or_404(Board, pk=pk)
	topics = board.topics.order_by('-last_updated').annotate(replies= Count('posts')-1)
	return render(request, 'topics.html', {'board':board, 'topics':topics})



