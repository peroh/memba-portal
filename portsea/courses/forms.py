from django import forms
from courses.models import Course, CourseType
from members.models import Member
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import ClearableFileInput

class CourseForm(forms.ModelForm):
    course_name = forms.CharField(max_length=Course.course_max_length)
    course_type = forms.ModelChoiceField(queryset=CourseType.objects.all())
    course_start_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label="---"))
    course_end_date = forms.DateField(required=False, widget=SelectDateWidget(empty_label="---"))
    # paperwork = forms.FileField(widget=ClearableFileInput, required=False)

    class Meta:
        model = Course
        fields = ['course_name', 'course_type', "course_start_date", "course_end_date"]

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].label = "Name of Course"
        self.fields['course_type'].label = "Award"
        self.fields['course_start_date'].label = "Start Date"
        self.fields['course_end_date'].label = "End Date"

class AddCourseMembers(forms.ModelForm):
    members = forms.ModelChoiceField(queryset=Member.objects.all())

    class Meta:
        model = Member
        exclude = ['user', 'date_of_birth', 'club']