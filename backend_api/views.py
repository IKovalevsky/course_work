from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .models import Buyer
from backend_api.forms import RegisterForm



@login_required
def profile_view(request):
    return render(request, 'profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("app:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)