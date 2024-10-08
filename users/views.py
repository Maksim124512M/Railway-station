from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserSignupForm


class UserSignupView(generic.FormView):
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/profile.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)