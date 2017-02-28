from django import forms
from courses.models import Course, CourseType
from members.models import Member
from django.forms.extras.widgets import SelectDateWidget

class CourseForm(forms.ModelForm):
    course_name = forms.CharField(max_length=Course.course_max_length)
    course_type = forms.ModelChoiceField(queryset=CourseType.objects.all())
    course_start_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label="---"))
    course_end_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label="---"))
    # paperwork = forms.FileField(widget=ClearableFileInput, required=False)

    class Meta:
        model = Course
        fields = ['course_name', 'course_type', 'course_start_date', 'course_end_date']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].label = "Name of Course"
        self.fields['course_type'].label = "Award"
        self.fields['course_start_date'].label = "Start Date"
        self.fields['course_end_date'].label = "End Date"

class AddCourseMembers(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ['course_type', 'course_name', 'course_start_date', 'course_end_date', 'club', 'members']

    def __init__(self, *args, **kwargs):
        course_id = kwargs.pop('course_id')
        # get members registered to course
        members_registered = Course.objects.get(id=course_id).members.all()
        # list of all members not registered to course
        members_not_registered = Member.objects.exclude(id__in=members_registered)
        super(AddCourseMembers, self).__init__(*args, **kwargs)
        self.fields['members'] = forms.ModelMultipleChoiceField(
            queryset=members_not_registered,
            widget=forms.CheckboxSelectMultiple
        )