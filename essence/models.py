from django.db import models


class Contact(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    adress = models.CharField('Адрес', max_length=250)
    deal_count = models.IntegerField('Количество сделок', null=True)

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'adress': self.adress,
            'deal_count': self.deal_count,
        }

class Deal(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=256, null=True)
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Контакт',
        null=True
    )

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'contact': self.contact.id if self.contact else None,
        }