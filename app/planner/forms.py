from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Appointment, CourseMomentRelation, Event, TestMoment, User, EventAppointment


class CourseTimeSlotForm(forms.ModelForm):
    class Meta:
        model = CourseMomentRelation
        fields = '__all__'
        widgets = {
            'allowed_tests': forms.CheckboxSelectMultiple
        }


class CheckBoxSelectMultipleBootstrap(forms.CheckboxSelectMultiple):
    template_name = 'planner/forms/widgets/multiple_input.html'
    option_template_name = 'planner/forms/widgets/checkbox_option.html'


class EventAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.INPUT_TYPES = {'checkbox': EventAppointmentForm.construct_checkbox,
                            'radio': EventAppointmentForm.construct_radio}
        self.checkbox_max_amount = {}
        self.event = kwargs.pop("event")
        fields = self.event.extras.get("fields")

        super().__init__(*args, **kwargs)

        if fields:
            self.add_extra_fields(fields)

    def clean(self):
        cleaned_data = self.cleaned_data

        if not ' ' in cleaned_data.get('name'):
            self.add_error('name', 'Geef alsjeblieft je voor- en achtenaam op.')

        for field_name, max_amount in self.checkbox_max_amount.items():
            if len(cleaned_data.get(field_name, [])) > max_amount:
                self.add_error(field_name, f'Kies maximaal {max_amount} opties.')

        return cleaned_data

    def add_extra_fields(self, fields):
        for field in fields:
            if (type := field.get('type')) not in self.INPUT_TYPES:
                raise EventAppointmentForm.UnsupportedFieldTypeException

            input_field = self.INPUT_TYPES[type](field)

            name = field.get('name')

            # remember max amount
            if (max_amount := field.get('max_amount')):
                self.checkbox_max_amount[name] = max_amount

            self.fields[name] = input_field

    @staticmethod
    def construct_checkbox(field):
        choices = [(item, item) for item in field['options']]
        required = field.get('required', False)
        return forms.MultipleChoiceField(label=field['name'], widget=CheckBoxSelectMultipleBootstrap(), choices=choices, required=required)

    @staticmethod
    def construct_radio(field):
        choices = [(item, item) for item in field['options']]
        required = field.get('required', False)
        return forms.ChoiceField(label=field['name'], widget=forms.RadioSelect(), choices=choices, required=required)


    class Meta:
        model = EventAppointment
        fields = ('name', 'student_nr','email', 'start_time')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Voor- en achtenaam',
            }),
            'student_nr': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.HiddenInput(),

        }

        error_messages = {
            'student_nr': {
                'invalid': "Ongeldig studentnummer."
            },
            'start_time': {
                'required': "Kies een tijd."
            },
        }



    class UnsupportedFieldTypeException(Exception):
        pass


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.test_moment: TestMoment = kwargs.pop("test_moment", None)

        super().__init__(*args, **kwargs)

    def clean_tests(self):
        cleaned_data = self.cleaned_data

        if self.test_moment and len(cleaned_data['tests']) > self.test_moment.max_tests:
            raise ValidationError(f"Kies maximaal {self.test_moment.max_tests} toetsjes.", code='invalid_test_amount')

        return cleaned_data['tests']

    class Meta:
        model = Appointment
        fields = ['student_name', 'student_nr', 'email', 'tests', 'start_time', ]
        widgets = {
            'tests': CheckBoxSelectMultipleBootstrap(),
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'student_nr': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.HiddenInput(),
        }

        error_messages = {
            'tests': {
                'required': "Kies minimaal één toetsje.",
            },
            'start_time': {
                'required': "Kies een tijd"
            },
            'student_nr': {
                'invalid': "Ongeldig studentnummer"
            },
        }


class EventForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data['event_type']._slot_length and not cleaned_data['_slot_length']:
            raise ValidationError('No length was provided')
        elif not cleaned_data['event_type']._location and not cleaned_data['location']:
            raise ValidationError('No locations was provided')
        print(f"{cleaned_data=}")
        return cleaned_data

    class Meta:
        exclude = ('',)
        model = Event


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
