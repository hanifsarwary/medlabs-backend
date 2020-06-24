from django.conf.urls import url
from django.urls import include

from djangoapps.appointments.api.v1.urls import urlpatterns as appointments_urls
from djangoapps.editable_texts.api.v1.urls import urlpatterns as editable_text_urls
from djangoapps.users.api.v1.urls import urlpatterns as users_urls


urlpatterns = [
    url(r'^v1/', include(appointments_urls)),
    url(r'^v1/', include(editable_text_urls)),
    url(r'^v1/', include(users_urls)),
]
