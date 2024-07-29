from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = {
        "name": user.name,
        "username": user.username,
        "department": user.department,
        "position": user.position,
        "phone": user.phone,
        "email": user.email,
        "created": user.created
    }
    return JsonResponse(user_profile)

@require_http_methods(["POST"])
def update_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.name = request.POST.get("name", user.name)
    user.username = request.POST.get("username", user.username)
    user.department = request.POST.get("department", user.department)
    user.position = request.POST.get("position", user.position)
    user.phone = request.POST.get("phone", user.phone)
    user.email = request.POST.get("email", user.email)
    user.save()
    return JsonResponse({"status": "success", "message": "User profile updated successfully."})
