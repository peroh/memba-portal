from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from custom_user_official.models import MyUser
from custom_user_official.admin import UserCreationForm
# from portsea import courses


def members(request):
    member_list = MyUser.objects.all()
    context_dict = {'member_list': member_list}
    return render(request, 'members/members.html', context_dict)


def add_member(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('members:add_member_success'))
        else:
            print(form.errors)

    return render(request, 'members/add_member.html', {'form': form})

def add_member_success(request):
    context_dict = {}
    return render(request, 'members/add_member_success.html', context_dict)