from django.shortcuts import render

def member_view(request):
    """Return a rendered profile view of member."""
    return render(request, 'profile.html',context={
        'username': request.user.username,
    })