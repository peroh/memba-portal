from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from members.forms import MemberForm
from myuser.forms import MyUserCreationFormPassword, MyUserCreationForm
from myuser.models import MyUser


def members(request):
    user_list = MyUser.objects.all()
    context_dict = {'user_list': user_list}
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
    return render(request, 'members/add_member.html', {'user_form': user_form, 'member_form': member_form})

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
        uf = MyUserCreationForm(request.POST, instance=user)
        mf = MemberForm(request.POST, instance=member)
        if uf.is_valid and mf.is_valid:
            uf.save(commit=True)
            mf.save(commit=True)
            return HttpResponseRedirect(reverse('members:member_detail', kwargs={'user_id': user_id}))

        else:
            print uf.errors, mf.errors
    else:
        uf = MyUserCreationForm(instance=user)
        mf = MemberForm(instance=member)

    context_dict_edit = {
        'uf': uf,
        'mf': mf,
        'user': user,
    }

    return render(request, 'members/member_edit.html', context=context_dict_edit)




def add_member_success(request):
    context_dict = {}
    return render(request, 'members/add_member_success.html', context_dict)