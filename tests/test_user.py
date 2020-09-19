""" 
class SettingsTest(TestCase):    
    def test_account_is_configured(self):
        self.assertTrue('accounts' in INSTALLED_APPS)
        self.assertTrue('accounts.User' == AUTH_USER_MODEL)


class UserTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.email = "testuser@testbase.com"
        self.first_name = "Test"
        self.last_name = "User"
        self.password = "z"

        self.test_user = User.objects.create_user(
            username=self.username,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_create_user(self):
        self.assertIsInstance(self.test_user, User)

    def test_default_user_is_active(self):
        self.assertTrue(self.test_user.is_active)

    def test_default_user_is_staff(self):
        self.assertFalse(self.test_user.is_staff)

    def test_default_user_is_superuser(self):
        self.assertFalse(self.test_user.is_superuser)

    def test_get_full_name(self):
        self.assertEqual('Test User', self.test_user.get_full_name())

    def test_get_short_name(self):
        self.assertEqual(self.email, self.test_user.get_short_name())

    def test_unicode(self):
        self.assertEqual(self.username, self.test_user.__unicode__())
""" 