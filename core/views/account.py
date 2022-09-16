from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views.generic import CreateView
from django.contrib.auth import (
    login, authenticate
)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from core.forms import (
    UserLoginForm, UserRegisterForm
    )

class LoginView(LoginView):
    redirect_authenticated_user = True
    authentication_form = UserLoginForm
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        return super().post(request, *args, **kwargs)

class LogoutView(LogoutView):
    template_name = 'logout.html'
    
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'account/signup.html'
    success_url = reverse_lazy('panel:lead:login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"