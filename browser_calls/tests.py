from django.test import TestCase, Client
from model_mommy import mommy

from .models import SupportTicket

# Import Mock if we're running on Python 2
import six

if six.PY3:  # pragma: no cover
    from unittest.mock import patch, MagicMock
else:  # pragma: no cover
    from mock import patch, MagicMock


class SupportTicketTest(TestCase):

    def test_str(self):
        # Arrange
        support_ticket = mommy.make(
            SupportTicket,
            name='Charles Holdsworth',
            phone_number='+15555555555',
            description='I have a problem!')

        # Assert
        self.assertEqual(str(support_ticket), '#{0} - {1}'.format(support_ticket.id, support_ticket.name))


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
            phone_number='+15555555555',
            description='I have a problem!')

        # Act
        response = self.client.get('/support/dashboard')

        # Assert
        self.assertEqual(len(response.context['support_tickets']), SupportTicket.objects.count())


class GetTokenTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_token_unauthenticated(self):
        # Arrange
        mock_capability = MagicMock()
        mock_capability.generate.return_value = 'abc123'

        # Act
        with patch('browser_calls.views.ClientCapabilityToken', return_value=mock_capability) as mock:
            response = self.client.get('/support/token', {'forPage': '/'})

        # Assert
        # Make sure our mock_capability object was called with the right
        # arguments and that the view returned the correct response
        self.assertTrue(mock_capability.allow_client_outgoing.called)
        mock_capability.allow_client_incoming.assert_called_once_with('customer')
        self.assertTrue(mock_capability.generate.called)

        self.assertEqual(response.content, b'{"token": "abc123"}')

    def test_get_token_authenticated(self):
        # Arrange
        mock_capability = MagicMock()
        mock_capability.generate.return_value = 'foo123'

        # Act
        with patch('browser_calls.views.ClientCapabilityToken', return_value=mock_capability) as mock:
            response = self.client.get('/support/token', {'forPage': '/support/dashboard'})

        # Assert
        self.assertTrue(mock_capability.allow_client_outgoing.called)
        mock_capability.allow_client_incoming.assert_called_once_with('support_agent')
        self.assertTrue(mock_capability.generate.called)

        self.assertEqual(response.content, b'{"token": "foo123"}')


class CallTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_call_phone_number(self):
        # Act
        response = self.client.post('/support/call', {'phoneNumber': '+15555555555'})

        # Assert
        self.assertIn('<Number>+15555555555</Number>', str(response.content))

    def test_call_support(self):
        # Act
        response = self.client.post('/support/call')

        # Assert
        self.assertIn('<Client>support_agent</Client>', str(response.content))
