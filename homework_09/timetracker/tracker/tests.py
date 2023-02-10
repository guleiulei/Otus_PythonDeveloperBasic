from django.test import TestCase
from .models import Task, Epic


class TestTask(TestCase):

    def test_str(self):
        epic = Epic.objects.create(epic_name='Quality')
        task = Task.objects.create(task_name='Презентация отчета', epic=epic)
        self.assertEqual(str(task), 'Презентация отчета')


class TestEpic(TestCase):

    def setUp(self) -> None:
        self.epic = Epic.objects.create(epic_name='Quality')

    def tearDown(self):
        self.epic.delete()

    def test_str(self):
        epic = Epic.objects.create(epic_name='Quality')
        self.assertEqual(str(epic), 'Quality')
