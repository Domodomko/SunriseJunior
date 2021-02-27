from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
import threading
from django.conf import settings


def run_in_thread(fn):
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.start()
    return run


@run_in_thread
def send_mail_with_token_link(request, mail_subject, user, to_email, token, template):
    current_site = get_current_site(request)
    message = render_to_string(template, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token.make_token(user),
    })
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False, )


@run_in_thread
def send_simple_mail(request, mail_subject, to_email, template):
    current_site = get_current_site(request)
    message = render_to_string(template, {
        'domain': current_site.domain,
    })
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False, )