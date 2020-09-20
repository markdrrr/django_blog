from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from blog.models import Post, Comment
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.all().filter(deleted=False, draft=False)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post__id=pk, deleted=False)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.author = request.user
            comment.date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
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
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.deleted = True
    post.save()
    return redirect('post_list')


def post_draft_list(request):
    user = request.user
    posts = Post.objects.filter(draft=True, author=user)
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.draft = False
    post.save()
    return redirect('post_detail', pk=pk)


# def login(request):
#     return redirect(request, 'registration/login.html')


def post_comment(request, pk):
    comments = Comment.objects.filter(post__id=pk, deleted=False)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.author = request.user
            comment.date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment.html', {'comments': comments, 'form': form})

def comment_remove(request, pk_comment):
    comment = get_object_or_404(Comment, pk=pk_comment)
    comment.deleted = True
    comment.save()
    pk_post = comment.post.pk
    return redirect('post_detail', pk=pk_post)

def comment_edit(request, pk_comment):
    comment = get_object_or_404(Comment, pk=pk_comment)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=comment.post.pk)
            comment.author = request.user
            comment.date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {'form': form})


