from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
from django.contrib import admin
from .models import Application, Department
from .token_generator import account_activation_token


# Create your views here.


def application_list(request):
    # e = Department.objects.get()
    get_all_applicants = Application.objects.all().order_by("-date_applied")
    # .select_related()
    return render(request, 'mail_app/application_list.html', {"get_all_applicants": get_all_applicants})


# Create your views here.

@csrf_exempt
def application(request):
    if request.method == 'POST':
        pno = request.POST['pno']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        other_name = request.POST['other_name']
        phone_no = request.POST['phone_no']
        designation = request.POST['designation']
        email = request.POST['email']
        department_name = request.POST['department_name']

        # GET ALL DEPARTMENTS INTO SELECT BUTTON

        # GET ALL APPLICATIONS

        applicant = Application.objects.create(pno=pno, last_name=last_name, first_name=first_name,
                                               other_name=other_name, email=email, phone_no=phone_no,
                                               designation=designation, department_select=department_name)

        # GET APPLICANT'S DEPARTMENT TO GET HOD EMAIL
        get_applicant_department = Department.objects.get(department_name=department_name)
        get_applicant_hod_email = get_applicant_department.department_hod_email
        print(get_applicant_department.department_hod_last_name)
        print(get_applicant_department.department_hod_first_name)

        #

        # SEND CONFIRMATION EMAIL TO HOD AND APPLICANT

        subject = 'Application for UCH Official Email'
        current_site = get_current_site(request)
        message_to_hod = render_to_string('activate_account.html', {
            'applicant': applicant,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(applicant.pk)),
            'token': account_activation_token.make_token(applicant),
        })
        msg_to_hod = (subject, message_to_hod, 'requestform@uch-ibadan.org.ng', [get_applicant_hod_email])
        msg_to_applicant = (subject,
                            'We have sent an email to your Head of Department to confirm your employment status '
                            'before we continue processing your application',
                            'requestform@uch-ibadan.org.ng', [email])

        send_mass_mail((msg_to_applicant, msg_to_hod), fail_silently=False)

        return HttpResponse(
            'We have sent an email to your Head of Department to confirm your employment status before we continue '
            'processing your application')

    else:
        departmentlists = Department.objects.all().order_by('department_name')

        return render(request, 'mail_app/application.html', {"departmentlists": departmentlists})

    # DISPLAY ALL APPLICANTIONS


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        applicant = Application.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Application.DoesNotExist):
        applicant = None
    if applicant is not None and account_activation_token.check_token(applicant, token):
        applicant.is_active = True
        applicant.save()

        #     SEND FEEDBACK TO APPLICANT
        send_mail(
            'RE:UCH official email request',
            'Your HOD has confirmed your employment status, Information Technology Department will send your official within 12hrs',
            'requestform@uch-ibadan.org.ng',
            [applicant.email],
            fail_silently=False,
        )
        # login(request, user)

        return HttpResponse('Your account has been activated successfully')
    else:
        return HttpResponse('Activation link is invalid!')

    admin.site.register(Department)
