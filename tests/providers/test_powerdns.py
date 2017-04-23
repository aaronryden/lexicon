from lexicon.providers.powerdns import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class PowerdnsProviderTests(TestCase, IntegrationTests):

	Provider = Provider
	provider_name = 'powerdns'
	domain = 'example.com'

	def _filter_headers(self):
		return ['X-API-Key']
