from django.shortcuts import render

def common_view(request):
    return render(request, 'common/common_view.html')
