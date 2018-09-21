from . import views
from django.urls import path


urlpatterns = [

    path("add_contact/", views.AddContact.as_view()),

    path("", views.ListContact.as_view(), name="new_contacts"),
    path("list-company/", views.ListCompany.as_view(), name="company"),

    path("update-contact/<int:pk>", views.UpdateContact.as_view(), name="update-contact"),
    path("delete-contact/<int:pk>", views.ContactDelete.as_view(), name='delete-contact'),


]

