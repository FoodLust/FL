from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Member
from django.contrib.auth.models import User

@login_required
def member_view(request):
    """Return a rendered member view of member."""
    all_meals = request.user.meal.all()
    return render(request, 'member.html',context={
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'meals': all_meals
    })

@login_required
class EditMemberView(UpdateView):
    """View for editing member info."""
    template_name = 'edit_member.html'
    model = User
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
    ]
    success_url = reverse_lazy('member')

    def get_object(self):
        return self.request.user