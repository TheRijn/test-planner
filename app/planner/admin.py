from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CourseTimeSlotForm, CustomUserChangeForm, CustomUserCreationForm
from .models import User, Course, TestMoment, Test, Appointment, CourseMoment


class CourseTimeSlotMemberInline(admin.TabularInline):
    model = CourseMoment
    extra = 1
    # One of these lines is the better solution :)
    form = CourseTimeSlotForm

class TestMomentAdmin(admin.ModelAdmin):
    inlines = (CourseTimeSlotMemberInline,)
    list_display = ('date','time_string', 'course_name_list')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', 'is_staff']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TestMoment, TestMomentAdmin)
admin.site.register(Test)
admin.site.register(Appointment)
