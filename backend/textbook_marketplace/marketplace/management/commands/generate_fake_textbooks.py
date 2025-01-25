from django.core.management.base import BaseCommand
from faker import Faker
from marketplace.models import Textbook, User
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Generate fake textbooks with specified count'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of textbooks to generate')

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        # Получаем случайных пользователей, которые будут продавцами учебников
        users = User.objects.filter(is_seller=True)

        if not users:
            self.stdout.write(self.style.ERROR('No sellers found! Please ensure you have sellers in the system.'))
            return

        for _ in range(count):
            title = fake.bs()  # Генерируем случайное название учебника
            author = fake.name()  # Случайное имя автора
            school_class = f'{random.randint(1, 11)}'  # Случайный класс от 1 до 11
            publisher = fake.company()  # Генерация названия издательства
            price = Decimal(random.uniform(5, 100))  # Случайная цена учебника
            seller = random.choice(users)  # Случайный продавец
            description = fake.text()  # Описание учебника
            whatsapp_contact = fake.phone_number()  # Контакт в WhatsApp
            viber_contact = fake.phone_number()  # Контакт в Viber
            telegram_contact = fake.phone_number()  # Контакт в Telegram
            phone_contact = fake.phone_number()  # Простой номер телефона
            condition = random.choice(['New', 'Used - Excellent', 'Used - Good', 'Used - Fair'])  # Состояние учебника
            image = None  # Для простоты оставляем без изображения

            # Создаем учебник
            textbook = Textbook.objects.create(
                title=title,
                author=author,
                school_class=school_class,
                publisher=publisher,
                price=price,
                seller=seller,
                description=description,
                whatsapp_contact=whatsapp_contact,
                viber_contact=viber_contact,
                telegram_contact=telegram_contact,
                phone_contact=phone_contact,
                condition=condition,
                image=image  # Если нужно, добавьте изображения вручную позже
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created textbook "{title}"'))
