""" User views."""

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView

#Forms
from users.forms import ProfileForm, SignupForm

# Models
from django.contrib.auth.models import User
from posts.models import Post

class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's post to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created_at')
        return context

class SignUpView(FormView):
    """ Register as a new user."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save the form data """
        form.save()
        return super().form_valid(form)

def login_view(request):
    """ Login View."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', { 'error': 'Invalid username and password' })

    return render(request, 'users/login.html')

@login_required()
def logout_view(request):
    """ Logout a user"""

    logout(request)
    return redirect('users:login')

@login_required()
def update_profile(request):
    """Update users profile view."""

    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request,
        'users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

