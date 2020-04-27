from unittest.mock import MagicMock, patch

from django.test import Client, TestCase
from model_mommy import mommy

from .models import SupportTicket


class SupportTicketTest(TestCase):
    def test_str(self):
        # Arrange
        support_ticket = mommy.make(
            SupportTicket,
            name='Charles Holdsworth',
            phone_number='+12027621401',
            description='I have a problem!',
        )

        # Assert
        self.assertEqual(
            str(support_ticket),
            '#{0} - {1}'.format(support_ticket.id, support_ticket.name),
        )


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        # Act
        response = self.client.get('/')

        # Assert
        # This is a class-based view, so we can mostly rely on Django's own
        # tests to make sure it works. We'll check for a bit of copy, though
        self.assertIn('sport of kings', str(response.content))


class SupportDashboardTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_support_dashboard(self):
        # Arrange
        support_ticket = mommy.make(
            SupportTicket,
            name='Charles Holdsworth',
            phone_number='+12027621401',
            description='I have a problem!',
        )

        # Act
        response = self.client.get('/support/dashboard')

        # Assert
        self.assertEqual(
            len(response.context['support_tickets']),
            SupportTicket.objects.count(),
        )


class GetTokenTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_token_unauthenticated(self):
        mock_access_token = MagicMock()
        mock_access_token.to_jwt.return_value = b'abc123'

        with patch(
            'browser_calls.views.AccessToken',
            return_value=mock_access_token
        ):
            response = self.client.get('/support/token', {'forPage': '/'})

        self.assertTrue(mock_access_token.add_grant.called)

        self.assertTrue(mock_access_token.to_jwt.called)

        self.assertEqual(response.content, b'{"token": "abc123"}')

    def test_get_token_authenticated(self):
        mock_access_token = MagicMock()
        mock_access_token.to_jwt.return_value = b'foo123'

        with patch(
            'browser_calls.views.AccessToken',
            return_value=mock_access_token
        ):
            response = self.client.get('/support/token', {'forPage': 'support/dashboard'})

        self.assertTrue(mock_access_token.add_grant.called)

        self.assertTrue(mock_access_token.to_jwt.called)

        self.assertEqual(response.content, b'{"token": "foo123"}')

class CallTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_call_phone_number(self):
        # Act
        response = self.client.post(
            '/support/call', {'phoneNumber': '+15555555555'}
        )

        # Assert
        self.assertIn('<Number>+15555555555</Number>', str(response.content))

    def test_call_support(self):
        # Act
        response = self.client.post('/support/call')

        # Assert
        self.assertIn('<Client>support_agent</Client>', str(response.content))
