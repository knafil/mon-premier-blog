from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime
from .models import Post
from .forms import PostForm, CommentaireForm
# Create your views here.
def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def login(request):
	return render(request, 'blog/login.html')

#def post_detail(request, pk):
#	post = get_object_or_404(Post, pk=pk)
#	return render(request, 'blog/post_detail.html', {'post': post})

def post_detail(request, pk):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    commentaires = post.commentaires.filter(active=True)
    new_comment = None
    if request.method == 'POST':
       comment_form = CommentaireForm(data=request.POST)
       if comment_form.is_valid():
          new_comment = comment_form.save(commit=False)
          new_comment.post = post
          new_comment.save()
    else:
          comment_form = CommentaireForm()
    return render(request, template_name, {'post': post, 'commentaires': commentaires, 'new_comment': new_comment, 'comment_form': comment_form})

def post_welcome(request):
	return render(request, 'blog/post_welcome.html',{'current_date_time':
datetime.now})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
       form = EmailPostForm(request.POST)
       if form.is_valid():
          cd = form.cleaned_data
    else:
       form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
