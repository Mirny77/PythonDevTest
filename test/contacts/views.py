from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.urls import reverse
import requests

from bs4 import BeautifulSoup


class AddContact(CreateView):
    """ Добавление
    """
    model = NewContact
    form_class = ContactForm
    template_name = "new_contact/add_contact.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect("/new_contact/add_contact/")

    def success_url(self):
        return redirect("/add_contact/")

class ListContact(ListView):
    """Список
            """
    model = NewContact
    queryset = NewContact.objects.all().order_by("-date")[:10]

    context_object_name = "new_contacts"
    template_name = "new_contact/contacts.html"

    # def get_queryset(self):
    #     return NewContact.objects.filter(name=self.request.name)

class UpdateContact(UpdateView):
    """Редактипрование тикета
    """
    model = NewContact
    form_class = ContactForm
    template_name = "new_contact/update-contacts.html"

    def get_success_url(self):
        return reverse('new_contacts')

class ContactDelete(DeleteView):
    model = NewContact
    template_name = 'new_contact/delete_contacts.html'

    def get_success_url(self):
        return reverse('new_contacts')
class ListCompany(ListView):
    """Список
            """
    model = Company
    queryset = Company.objects.all()

    context_object_name = "company"
    template_name = "company.html"


def parse(request):


    url = 'http://breffi.ru/ru/about/'
    page = requests.get(url, verify=False).text

    soup = BeautifulSoup(page, "html.parser")
    divs = soup.findAll("div", {'class': 'content-section__item'})

    for div in divs:
        div_title = div.find('div', {'class': 'content-section__itemtitle'}).text
        print(div_title)
    return render(request,'new_contact/contacts.html',locals())