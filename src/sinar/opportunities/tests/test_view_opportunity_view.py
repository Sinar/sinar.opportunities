# -*- coding: utf-8 -*-
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_FUNCTIONAL_TESTING
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_INTEGRATION_TESTING
from sinar.opportunities.views.opportunity_view import IOpportunityView
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

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

    def test_opportunity_view_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='opportunity-view'
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = IOpportunityView.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = SINAR_OPPORTUNITIES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
