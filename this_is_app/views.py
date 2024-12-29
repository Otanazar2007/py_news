from audioop import reverse

from django.contrib.auth.decorators import login_required
#from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from this_is_app.models import Post, CategoryPost, Commentary, Likes,PredlojennieNovosti
from django.contrib import messages
from user.forms import PredlojenieNovostiForm
# Create your views here.

def home_page(request):
    if request.method == 'POST':
        post = Post.objects.all()
        categories = CategoryPost.objects.all()
        return render(request, 'this_is_app/home.html',
                      {'post':post,
                       'categories':categories})
    else:
        post = Post.objects.all()
        categories = CategoryPost.objects.all()
        return render(request, 'this_is_app/home.html',
                      {'post':post,
                       'categories':categories})


@login_required
def comment_view(request):
    if request.method == 'POST':
        all_comments = Commentary.objects.all()
        return render(request, 'this_is_app/comments_page.html',
                      {'all_comments':all_comments})
    else:
        all_comments = Commentary.objects.all()
        return render(request, 'this_is_app/comments_page.html',
                      {'all_comments':all_comments})


@login_required()
def add_comment(request, pk):
    if request.method == 'POST':
        try:
            comment_text = request.POST.get('comment', '').strip()
            print(f'Это коммент {comment_text}')
            if comment_text:
                post = Post.objects.get(id = pk)
                Commentary.objects.create(
                    post_comment = post,
                    commentary_text = comment_text,
                    username = request.user
                )
                next_url = request.POST.get('next')
                return redirect(next_url)
        except Post.DoesNotExist:
            messages.error(request, 'Бля иди нахуй')
    else:
        return redirect('home')


def comment(request, pk):
    if request.method == 'POST':
        try:
            new = Post.objects.get(id = pk)
            comments = Commentary.objects.filter(
                post_comment = new.id
            )
            print(comments)
            if comments.exists():
                comments = comments
            else:
                comments = []
            return render(request, 'this_is_app/comments_page.html',
                            {'new': new,
                            'comments': comments})
        except Post.DoesNotExist:
            redirect('home')
            pass
        except Exception as e:
            pass
    else:
        return redirect('home')

@login_required()
def like(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id = pk)
        if Likes.objects.filter(username = request.user, like_post = post).exists():
            messages.warning(request, 'Лайк уже есть')
        else:
            Likes.objects.create(
                like_post = post,
                username = request.user
            )
            post.like_post +=1
            post.save()
        return redirect('home')
    else:
        return redirect('home')

@login_required()
def predlojen_nov(request):
    if request.method == 'POST':
        form = PredlojenieNovostiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_post = form.save(commit=False)
            new_post.post_from_user = request.user
            new_post.save()
            messages.success(request, 'Успех')
            return redirect('home')
        else:
            messages.warning(request, 'Чето не так')
            return redirect('home')
    else:
        return redirect('home')