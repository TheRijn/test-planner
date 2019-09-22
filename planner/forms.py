from django import forms
from .models import Test, Course, Appointment

class CheckBoxSelectMultipleBootstrap(forms.CheckboxSelectMultiple):
    template_name = 'planner/forms/widgets/multiple_input.html'
    option_template_name = 'planner/forms/widgets/checkbox_option.html'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['student_name', 'email', 'tests']
        widgets = {
            'tests': CheckBoxSelectMultipleBootstrap(),
            'student_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
