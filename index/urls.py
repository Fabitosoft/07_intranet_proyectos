from django.urls import path, include

from .views import (
    IndexView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('app/*', IndexView.as_view(), name='index'),
    path('accounts/', include('registration.backends.default.urls')),
]
