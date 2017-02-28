from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from members.forms import MemberForm
from myuser.forms import MyUserCreationForm
from myuser.models import MyUser


def members(request):
    user_list = MyUser.objects.all()

    context_dict = {
        'user_list': user_list
    }
    return render(request, 'members/members.html', context_dict)


def add_member(request):
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST, prefix='user')
        member_form = MemberForm(request.POST, prefix='userprofile')
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            return HttpResponseRedirect(reverse('members:add_member_success'))
    else:
        user_form = MyUserCreationForm(prefix='user')
        member_form = MemberForm(prefix='member')

    context_dict = {
        'user_form': user_form,
        'member_form': member_form,
    }
    return render(request, 'members/add_member.html', context_dict)


def member_detail(request, user_id):
    user = MyUser.objects.get(pk=user_id)

    context_dict = {
        'user': user,
    }
    return render(request, 'members/member_detail.html', context_dict)


def edit_member(request, user_id):
    user = MyUser.objects.get(pk=user_id)
    member = user.member

    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST, instance=user)
        member_form = MemberForm(request.POST, instance=member)
        if user_form.is_valid and member_form.is_valid:
            user_form.save(commit=True)
            member_form.save(commit=True)
            return HttpResponseRedirect(reverse(
                'members:member_detail',
                kwargs={'user_id': user_id},
                ))
        else:
            print user_form.errors, member_form.errors
    else:
        user_form = MyUserCreationForm(instance=user)
        member_form = MemberForm(instance=member)

    context_dict = {
        'user_form': user_form,
        'member_form': member_form,
        'user': user,
    }
    return render(request, 'members/member_edit.html', context_dict)


def add_member_success(request):
    context_dict = {}
    return render(request, 'members/add_member_success.html', context_dict)