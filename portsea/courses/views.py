from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from courses.models import Course, PaperworkHistory
from courses.forms import CourseForm


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


def edit_course(request, course_id=None):
    if course_id:
        course = Course.objects.get(pk=course_id)
    else:
        course = None

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid:
            form.save(commit=True)
            if course_id:
                return HttpResponseRedirect(reverse('courses:course_detail', kwargs={'course_id': course_id}))
            else:
                return HttpResponseRedirect(reverse('courses:courses'))
        else:
            print form.errors
    else:
        form = CourseForm(instance=course)

    context_dict_edit = {
        'form': form,
        'course': course,
    }
    context_dict_add = {
        'form': form,
    }

    if course_id:
        return render(request, 'courses/course_edit.html', context=context_dict_edit)
    else:
        return render(request, 'courses/course_add.html', context=context_dict_add)


def download_pdf(request, paperwork_id, download_type):

    paperwork = PaperworkHistory.objects.get(pk=paperwork_id)
    path = paperwork.paperwork.path

    with open(path, 'rb') as pdf:
        response = HttpResponse(pdf.read())
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = download_type + ';filename=file.pdf'
        return response
