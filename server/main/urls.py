from django.urls import path, include
from main.views import (
    main_view, contacts_view, about_view
)

urlpatterns = [
    path("",main_view),
    path("contacts/",contacts_view),
    path("about/",about_view),
]