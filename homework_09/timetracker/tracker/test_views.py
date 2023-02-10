from django.test import TestCase


class TestTaskListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/task-list/')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get('/task-list/')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'Тебе в помощь')

