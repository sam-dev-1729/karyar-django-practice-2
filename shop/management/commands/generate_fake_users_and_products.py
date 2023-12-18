from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from faker import Faker

from shop.models import Category, Product

User = get_user_model()


class Command(BaseCommand):
    help = "Generate fake data for testing"

    def add_arguments(self, parser):
        parser.add_argument(
            "number-of-users",
            type=int,
            help="Indicates the number of fake users to be created",
        )

        parser.add_argument(
            "number-of-products",
            type=int,
            help="Indicates the number of fake products to be created",
        )

    def handle(self, *args, **kwargs):
        users_num = kwargs["number-of-users"]
        products_num = kwargs["number-of-products"]

        self.stdout.write(
            self.style.SUCCESS(f"Generating {users_num} fake users...")
        )
        self.generate_fake_users(users_num)

        self.stdout.write(
            self.style.SUCCESS(f"Generating {products_num} fake products ...")
        )
        self.generate_fake_products(products_num)

    def generate_fake_users(self, users_num):
        for index in range(users_num):
            fake = Faker()
            user_name = fake.user_name() + str(index)
            email = fake.email()
            password = get_random_string(length=12)
            User.objects.create_user(
                username=user_name, email=email, password=password
            )

    def generate_fake_products(self, products_num):
        category_list = Category.objects.all()

        for index in range(products_num):
            fake = Faker()
            name = fake.word()
            price = fake.random_int(min=5, max=120)
            user = User.objects.order_by("?").first()
            product = Product.objects.create(name=name, price=price, user=user)

        product.categories.set(
            category_list.order_by("?")[: fake.random_int(min=1, max=3)]
        )
