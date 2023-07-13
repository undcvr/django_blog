from typing import Any, Dict
from django.shortcuts import render
from django.utils import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import regex
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, FormView
# from django.contrib.auth.mixins import LoginRequiredMixin

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


# @login_required
# def profile(request):
#     # profile = Profile.objects.create(user=request.user)
#     profile = request.user.profile
#     return render(request, 'profile/profile.html', {'profile': profile})

# @login_required
# def edit_profile(request):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile:profile')
#     else:
#         form = ProfileForm(instance=profile)
#     return render(request, 'profile/edit_profile.html', {'form': form})

# def profile_view(request, pk=None):
#     profiles = get_object_or_404(Profile, pk=pk)
#     return render(request, 'profile/profile_view.html', {'profiles': profiles})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/mainpage.html', {'posts': posts, })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'blog/base.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})