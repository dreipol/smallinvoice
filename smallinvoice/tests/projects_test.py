# coding=utf-8
import unittest
from smallinvoice.projects import Project
from smallinvoice.tests import get_smallinvoice, generate_customer, \
    generate_address


def generate_project():
    return Project(
        name='Testproject',
        client_id=''
    )


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.address = generate_address()
        self.client = generate_customer()
        self.client.add_address(self.address)
        self.project = generate_project()
        self.customer_id = get_smallinvoice().clients.add(self.client)
        self.project.client_id = self.customer_id
        self.project_id = get_smallinvoice().projects.add(self.project)

    def tearDown(self):
        get_smallinvoice().clients.delete(self.customer_id)
        get_smallinvoice().projects.delete(self.project_id)

    def test_project(self):
        self.assertIsNotNone(self.project_id)

    def test_project_details(self):
        self.assertEqual(self.project.name, 'Testproject')

    def test_project_update(self):
        self.assertEqual(self.project.name, 'Testproject')
        self.project.name = 'AV-Framing'
        self.assertEqual(self.project.name, 'AV-Framing')
