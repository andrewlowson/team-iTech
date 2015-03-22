from django.test import TestCase
from rango.models import Celebrity

class CelebrityTests(TestCase):
    def test_ensure_views_are_positive(self):

        celebrity = Celebrity(name='test', views=-1, likes=0)
        celebrity.save()
        self.assertEqual((celebrity.views >= 0), True)


from django.core.urlresolvers import reverse

class IndexViewTests(TestCase):
    def test_index_view(self):
        """

        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no celebrities in the database")
        self.assertQuerysetEqual(response.context['celebrities'], [])