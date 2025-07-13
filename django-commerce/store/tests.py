from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User



class ProductViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TVV", slug='tv')
        self.user = User.objects.create_user(username="testuser", password="pass123")
        image = SimpleUploadedFile(name='test.jpg', content=b'\x47\x49\x46', content_type="image/jpeg")
        self.product = Product.objects.create(
            name='Test Tvv',
            description = "mamita",
            stock = 10,
            image = image,
            price=499.99,
            category=self.category

        )

   
    def test_homepage_status_code(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
  

    def test_product_name_appears_on_homepage(self):
        from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User



class ProductViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TVV", slug='tv')
        self.user = User.objects.create_user(username="testuser", password="pass123")
        image = SimpleUploadedFile(name='test.jpg', content=b'\x47\x49\x46', content_type="image/jpeg")
        self.product = Product.objects.create(
            name='Test Tvv',
            description = "mamita",
            stock = 10,
            image = image,
            price=499.99,
            category=self.category

        )

   
    def test_homepage_status_code(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
  

    def test_product_name_appears_on_homepage(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.product.name)

    def test_login(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)


    def test_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_product_list(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get(reverse("product_detail", args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)


    def test_cart(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)


    def test_add_to_cart(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("add_to_cart", args=[self.product.pk]),{
            'color':'Black',
            'size':'Medium'
        })
        self.assertEqual(response.status_code, 302)


    def test_remove_from_cart(self):
        self.client.login(username="testuser", password="pass123")
        self.client.get(reverse("add_to_cart", args=[self.product.pk]), {
        'color': 'Black',
        'size': 'Medium'
    })
        response = self.client.get(reverse("remove_from_cart", args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)



    def test_checkout(self):
        self.client.login(username="testuser", password="pass123")
        self.client.get(reverse("add_to_cart", args=[self.product.pk]), {
        'color': 'Black',
        'size': 'Medium'
    })
        response = self.client.get(reverse("checkout"))
        self.assertEqual(response.status_code, 200)



    def test_order_confirmation(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("order_confirmation"))
        self.assertEqual(response.status_code, 200)


    def test_profile_update(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.get(reverse("profile_update"))
        self.assertEqual(response.status_code, 200)







