from phone_field import PhoneField
from rest_framework_simplejwt.tokens import RefreshToken
from django_rest_passwordreset.signals import reset_password_token_created

from django.conf import settings
from django.contrib.auth.models import AbstractUser as django_user
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from djangoapps.users.tasks import send_email


class User(django_user):
    """
    The User's model.
    """
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    address = models.TextField(blank=True, null=True)
    phone = PhoneField(blank=True, null=True)

    @property
    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip() or None

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.set_password(self.password)
        super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=User)
def send_verification_mail(sender, instance, created, **kwargs):
    """
    Send user account activation email.
    """
    if not created:
        return

    token = str(RefreshToken.for_user(instance).access_token)
    subject = 'Email Verification'
    message = 'Kindly follow the following link to verify your account.\n{}?token={}'.format(
        settings.ACTIVATION_EMAIL_DOMAIN + reverse('activate_view'),
        token
    )
    send_email.delay([instance.email], subject, message)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Send password reset email to user.
    """
    subject = 'Email Reset'
    message = 'Kindly follow the below mentioned link to reset your password.\n{}?token={}'.format(
        settings.ACTIVATION_EMAIL_DOMAIN + reverse('password_reset:reset-password-request'),
        reset_password_token.key,
    )
    send_email.delay([reset_password_token.user.email], subject, message)

