# -*- coding: utf-8 -*-
from sinar.opportunities.behaviors.opportunity_deadline import IOpportunityDeadlineMarker
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class OpportunityDeadlineIntegrationTest(unittest.TestCase):

    layer = SINAR_OPPORTUNITIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_opportunity_deadline(self):
        behavior = getUtility(IBehavior, 'sinar.opportunities.opportunity_deadline')
        self.assertEqual(
            behavior.marker,
            IOpportunityDeadlineMarker,
        )
