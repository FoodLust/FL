from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm


@login_required
def member_view(request):
    """Return a rendered member view of member."""
    all_meals = request.user.meal.all()
    # import pdb; pdb.set_trace()
    return render(request, 'member.html',context={
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'meals': all_meals,
        'follows': [follow for follow in request.user.member.following.all()],
        'followers': [person for person in request.user.member.followers.all()],
    })


class UserForm(ModelForm):
    """New user registration form"""
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email']


@login_required
def edit_member_view(request):
    """Edit member view."""
    template_name = 'edit_member.html'
    user = request.user
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('member')
    return render(request, template_name, {'form': form})
