from django.test import TestCase
from django.urls import reverse

from .models import Board
# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name = 'Java', description='Java problem resolved.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 23})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
