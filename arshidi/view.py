from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin')
    return render(request, 'index.html', {})
