from django.db import models


class Contact(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    adress = models.CharField('Адрес', max_length=250)
    deals = models.IntegerField('Сделка', null=True)

    def toDict(self):
        return {
            'id':self.id,
            'name': self.name,
            'phone': self.phone,
            'adress': self.adress,
            'deals': self.deals
        }