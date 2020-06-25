from celery.task import task

from django.core.mail.message import EmailMessage


@task()
def send_email(recipient_list, subject, body):
    """
    Send email according to given parameters.
    """
    message = EmailMessage()
    message.to = recipient_list
    message.subject = subject
    message.body = body
    try:
        message.send(fail_silently=False)
    except Exception:
        raise
