from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from courses.models import Course, PaperworkHistory
from courses.forms import CourseForm, AddCourseMembers
from members.models import Member


def courses(request):
    course_list = Course.objects.all()
    context_dict = {'course_list': course_list}
    return render(request, 'courses/courses.html', context_dict)


def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    paperwork_history = course.paperworkhistory_set.all()

    context_dict = {
        'course': course,
        'paperwork_history': paperwork_history,

    }
    return render(request, 'courses/course_detail.html', context_dict)

def add_course(request):

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('courses:courses'))
        else:
            print form.errors

    form = CourseForm()

    context_dict = {
        'form': form,
    }

    return render(request, 'courses/course_add.html', context=context_dict)


def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid:
            form.save(commit=True)
            return HttpResponseRedirect(reverse('courses:course_detail', kwargs={'course_id': course_id}))
        else:
            print form.errors
    else:
        form = CourseForm(instance=course)

    context_dict = {
        'form': form,
        'course': course,
    }

    return render(request, 'courses/course_edit.html', context=context_dict)



def course_members(request, course_id):
    course = Course.objects.get(pk=course_id)
    member_list = course.members.all()
    context_dict = {
        'member_list': member_list,
        'course': course
    }
    return render(request, 'courses/course_members.html', context_dict)

def add_course_members(request, course_id):

    course = Course.objects.get(pk=course_id)
    form = AddCourseMembers(course_id=course_id)
    members_not_registered = Member.objects.exclude(id__in=(Course.objects.get(id=course_id).members.all()))
    print members_not_registered

    if request.method == 'POST':
        form = AddCourseMembers(request.POST, course_id=course_id)
        if form.is_valid():
            new_members = form.cleaned_data['members']
            for member in new_members:
                course.members.add(member)
            return HttpResponseRedirect(reverse('courses:course_members', kwargs={'course_id':course.id}))
        else:
            print form.errors

    context_dict = {
        'course': course,
        'form': form,
        'members_not_registered': members_not_registered,
    }

    return render(request, 'courses/course_add_members.html', context_dict)


def download_pdf(request, paperwork_id, download_type):

    paperwork = PaperworkHistory.objects.get(pk=paperwork_id)
    path = paperwork.paperwork.path

    with open(path, 'rb') as pdf:
        response = HttpResponse(pdf.read())
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = download_type + ';filename=file.pdf'
        return response
