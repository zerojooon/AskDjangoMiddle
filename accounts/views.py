from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

@login_required
def profile(request):
    # request.user
    return render(request, 'accounts/profile.html')

#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             next_url = request.GET.get('next') or 'profile'
#             return redirect('profile')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup/html',{
#         'form':form
#     })


# signup = CreateView.as_view(model= User, form_class = UserCreationForm,
#                             template_name='accounts/signup.html',
#                             success_url=settings.LOGIN_URL)

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()