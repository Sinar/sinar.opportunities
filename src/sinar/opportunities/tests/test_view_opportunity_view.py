# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_FUNCTIONAL_TESTING
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_INTEGRATION_TESTING
from sinar.opportunities.views.opportunity_view import IOpportunityView
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = SINAR_OPPORTUNITIES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_opportunity_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='opportunity-view'
        )
        self.assertTrue(IOpportunityView.providedBy(view))

    def test_opportunity_view_registered_for_all_content(self):
        # The opportunity-view is registered with for="*", so it is
        # resolvable for any content type, including a plain document.
        view = getMultiAdapter(
            (self.portal['front-page'], self.portal.REQUEST),
            name='opportunity-view'
        )
        self.assertTrue(IOpportunityView.providedBy(view))


class ViewsFunctionalTest(unittest.TestCase):

    layer = SINAR_OPPORTUNITIES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
