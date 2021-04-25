from django.test import TestCase
from mainapp.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="Одежда")
        self.product_1 = Product.objects.create(name="Шапка 1",
                                                category=category,
                                                price=1999.5,
                                                quantity=150)

        self.product_2 = Product.objects.create(name="Перчатка 2",
                                                category=category,
                                                price=2998.1,
                                                quantity=125)

        self.product_3 = Product.objects.create(name="Перчатка 3",
                                                category=category,
                                                price=998.1,
                                                quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="Шапка 1")
        product_2 = Product.objects.get(name="Перчатка 2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="Шапка 1")
        product_2 = Product.objects.get(name="Перчатка 2")
        self.assertEqual(str(product_1), 'Шапка 1 | Одежда')
        self.assertEqual(str(product_2), 'Перчатка 2 | Одежда')

    # Построение модели отлично от изначального,
    # тест невозможен из-за отсутствия метода модели, работа осуществляется через контроллеры

    # def test_product_get_items(self):
    #     product_1 = Product.objects.get(name="Шапка 1")
    #     product_3 = Product.objects.get(name="Перчатка 3")
    #     products = product_1.get_all_products()

    # self.assertEqual(list(products), [product_1, product_3])
