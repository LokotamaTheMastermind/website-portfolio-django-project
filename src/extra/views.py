from django.shortcuts import render


def privacy(request):
    context = {}
    return render(request, 'extra/privacy.html', context)


def terms_conditions(request):
    context = {}
    return render(request, 'extra/terms-and-conditions.html', context)


def page_not_found(request, exception):
    context = {}
    return render(request, 'errors/404.html', context)


def server_error(request):
    context = {}
    return render(request, 'errors/500.html', context)
