from django.contrib.auth.views import LoginView
class LoginCustomView(LoginView):
    template_name ='accounts/login.html'

# Create your views here.
