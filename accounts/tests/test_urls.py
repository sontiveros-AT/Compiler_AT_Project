from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import user_reg_view

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_reg_view.UserRegisterView)
