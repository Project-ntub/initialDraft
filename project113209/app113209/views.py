from django.shortcuts import render
# 如果你使用了自定義 User 模型，確保它被正確導入
# from app113209.models import User  
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

class CustomLoginView(LoginView):
    template_name = 'login.html'  # 確保這個模板在你的模板目錄中

    @method_decorator(csrf_protect)  # 確保登入視圖被 CSRF 保護
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomLogoutView(LogoutView):
    next_page = 'login'  # 確保有一個名為 'login' 的 URL 可以重定向到


def register_view(request):
    # 實現用戶註冊邏輯
    return render(request, 'register.html')