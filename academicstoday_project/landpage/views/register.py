from django.shortcuts import render
from django.core import serializers

from landpage.models import LandpageTeamMember
from landpage.models import LandpageTopPickCourse
from landpage.models import LandpageCoursePreview
from landpage.models import CoursePreview
from landpage.models import LandpageContactMessage
from landpage.models import LandpagePartner
from registrar.models import Course
from landpage.form import RegisterForm

import json
from django.http import HttpResponse
from django.conf import settings


def register_modal(request):
    form = RegisterForm()
    return render(request, 'landpage/register/modal.html',{
        'form': form,
    })