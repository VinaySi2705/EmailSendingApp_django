from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail

from django.views import View
from django.conf import settings



class EmailView(View):

    def get(self,request):

        return render(request, "app/home.html")

    def post(self,request):

        subject = request.POST.get('subject')
        message = request.POST.get('message')

        html_message = render_to_string('app/email_page.html' , {"email": request.POST.get('email')})
        plain_message = strip_tags(html_message)
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = []
        recipient_list.append(request.POST.get('email') )

        send_mail(subject, message , email_from ,recipient_list , html_message=html_message)

        return render(request, "app/home.html" , {"message" : "succesfully send email"})
