from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class FrontendLoginView(LoginView):
    template_name = 'frontend/login.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontend-home')  # 成功登录后重定向到前台首页
        else:
            return render(request, self.template_name, {'error': 'Invalid username or password'})

def home(request):
    return render(request, 'frontend/home.html')
