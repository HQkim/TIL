from articles.models import Article
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.title = title
        article.content = content
        article.save()
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
