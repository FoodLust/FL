from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def member_view(request):
    """Return a rendered profile view of member."""
    all_meals = request.user.meal.all()
    return render(request, 'profile.html',context={
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'meals': all_meals
    })