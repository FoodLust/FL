from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def member_view(request):
    """Return a rendered profile view of member."""
    return render(request, 'profile.html',context={
        'username': request.user.username,
    })