from django.db.models.signals import post_save
from django.dispatch import receiver
from registration.models import NewUser
from category.models import Category

default_category = ["Забота о себе", "Зарплата", "Здоровье и фитнес", "Кафе и рестораны", "Машина",
                    "Образование", "Отдых и развлечения", "Платежи, комиссии", "Покупки: одежда, техника", "Продукты",
                    "Проезд"]


@receiver(post_save, sender=NewUser)
def handler(sender, **kwargs):
    if not sender.objects.last().is_superuser and kwargs['created'] is True:
        for a in default_category:
            Category.objects.create(name=a, user=sender.objects.last())
