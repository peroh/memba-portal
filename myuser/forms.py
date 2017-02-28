from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from myuser.models import MyUser


class MyUserCreationForm(forms.ModelForm):
    """To create new users without seeing password fields."""

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'is_active')

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class MyUserCreationFormPassword(forms.ModelForm):
    """To create new users seeing the password fields e.g. for admin."""

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MyUserCreationFormPassword, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                   "this user's password, but you can change the password "
                   "using <a href=\"../password/\">this form</a>."),
    )

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'last_name', 'is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
