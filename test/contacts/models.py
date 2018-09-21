from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField("Название компании ", max_length=156)
    country = models.CharField("Страна",max_length=254)
    region = models.CharField("Область",max_length=254)
    city = models.CharField("Город", max_length=254)
    street = models.CharField("Улица", max_length=254)
    house = models.CharField("Дом", max_length=64,blank=True, null=True)
    office = models.CharField("Офис",max_length=64,blank=True, null=True)


    def __str__(self):
        return "Компании %s " % self.name
    class Meta:

        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'







class NewContact(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, related_name='user_ind_provider_profile')

    # name = models.CharField("Имя", max_length=156)
    company = models.ManyToManyField(Company, verbose_name="Компания")
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=254)
    interest = models.TextField("Интерес", max_length=254)




    def __str__(self):
        return "Новые контакты %s " % self.name
    class Meta:

        verbose_name = 'Новый контакт'
        verbose_name_plural = 'Новые контакты'

