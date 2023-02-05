from django.db import models


CHOICES = (
            ('Малоэтажное строительство', 'Малоэтажное строительство'),
            ('Жилой комплекс', 'Жилой комплекс'),
            ('Коммерческая недвижимость', 'Коммерческая недвижимость'),
            ('Ж/Б конструкции', 'Ж/Б конструкции'),
            ('Навесные вентилируемые фасады', 'Навесные вентилируемые фасады'),
            ('Другое', 'Другое'),
        )

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=300, choices=CHOICES, default='')


    message = models.CharField(max_length=2000, null=True, blank=True)
    file = models.FileField(upload_to='', null=True, blank=True)

    def __str__(self):
        return f"{self.email_address}"
