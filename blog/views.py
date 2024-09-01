from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Category
from .forms import PostForm
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    FormView
)

# 메인 페이지 뷰
class MainView(TemplateView):
    template_name = 'blog/main.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.order_by('-created_at')[:5]
        return context

# 게시글 목록 뷰
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        category_slug = self.request.GET.get('category')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '') 
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '') 
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
  
    def get_object(self):
        post = super().get_object()
        post.views += 1  # 조회수 증가
        post.save()
        return post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
#    fields = ['title', 'content', 'tags', 'category'] 
# Specifying both 'fields' and 'form_class' is not permitted.
# "fields"와 "form_class"를 동시에 지정하는 것은 허용되지 않습니다.
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff  


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff 


class PostLikeToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if request.user in post.likes.all():
            post.likes.remove(request.user)  
        else:
            post.likes.add(request.user)  
        return redirect('post_detail', pk=post.pk)
    
class PostDislikeToggleView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)  
        else:
            post.dislikes.add(request.user)  
            if request.user in post.likes.all():
                post.likes.remove(request.user)  
        return redirect('post_detail', pk=post.pk)



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff  

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

class RegisterView(FormView):
    template_name = 'registration/register.html'  
    form_class = UserCreationForm
    success_url = reverse_lazy('main')  

    def form_valid(self, form):
        user = form.save()  
        login(self.request, user)  
        return super().form_valid(form)