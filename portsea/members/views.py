from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from custom_user_official.models import MyUser
from custom_user_official.admin import UserCreationForm
from members.forms import MemberForm


def members(request):
    member_list = MyUser.objects.all()
    context_dict = {'member_list': member_list}
    return render(request, 'members/members.html', context_dict)


def add_member(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST, prefix='user')
        upf = MemberForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect(reverse('members:add_member_success'))
    else:
        uf = UserCreationForm(prefix='user')
        upf = MemberForm(prefix='userprofile')
    return render(request, 'members/add_member.html', {'uf': uf, 'upf': upf})


def add_member_success(request):
    context_dict = {}
    return render(request, 'members/add_member_success.html', context_dict)