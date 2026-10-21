from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter

def news_list(request):
    news = Post.objects.filter(type=Post.NEWS).order_by('-created_at')
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'news': page_obj})

def news_search(request):
    f = PostFilter(request.GET, queryset=Post.objects.filter(type=Post.NEWS).order_by('-created_at'))
    return render(request, 'news_search.html', {'filter': f})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news_detail.html', {'post': post})

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import PostForm

class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')
    extra_context = {'title': 'Создать новость'}

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author
        post.type = Post.NEWS
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')
    extra_context = {'title': 'Редактировать новость'}

class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
    extra_context = {'title': 'Удалить новость'}

class ArticleCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('article_list')
    extra_context = {'title': 'Создать статью'}

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.author
        post.type = Post.ARTICLE
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('article_list')
    extra_context = {'title': 'Редактировать статью'}

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('article_list')
    extra_context = {'title': 'Удалить статью'}

def article_list(request):
    articles = Post.objects.filter(type=Post.ARTICLE).order_by('-created_at')
    return render(request, 'news_list.html', {'news': articles})