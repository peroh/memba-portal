from django import forms
from courses.models import Course, CourseType
from members.models import User
from authtools.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser

# class MemberForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=Member.max_name_length, help_text="First Name")
#     last_name = forms.CharField(max_length=Member.max_name_length, help_text="Last Name")
#     # email = forms.EmailField(widget=forms.EmailField, help_text="Email")
#
#     class Meta:
#         model = Member
#         fields = ('first_name', 'last_name')