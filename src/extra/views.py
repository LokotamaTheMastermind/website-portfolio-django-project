from django.shortcuts import render


def privacy(request):
    context = {}
    return render(request, 'extra/privacy.html', context)


def terms_conditions(request):
    context = {}
    return render(request, 'extra/terms-and-conditions.html', context)
