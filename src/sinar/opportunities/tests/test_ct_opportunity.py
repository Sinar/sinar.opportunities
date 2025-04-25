# -*- coding: utf-8 -*-
from sinar.opportunities.content.opportunity import IOpportunity  # NOQA E501
from sinar.opportunities.testing import SINAR_OPPORTUNITIES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class OpportunityIntegrationTest(unittest.TestCase):

    layer = SINAR_OPPORTUNITIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_opportunity_schema(self):
        fti = queryUtility(IDexterityFTI, name='Opportunity')
        schema = fti.lookupSchema()
        self.assertEqual(IOpportunity, schema)

    def test_ct_opportunity_fti(self):
        fti = queryUtility(IDexterityFTI, name='Opportunity')
        self.assertTrue(fti)

    def test_ct_opportunity_factory(self):
        fti = queryUtility(IDexterityFTI, name='Opportunity')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOpportunity.providedBy(obj),
            u'IOpportunity not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_opportunity_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Opportunity',
            id='opportunity',
        )

        self.assertTrue(
            IOpportunity.providedBy(obj),
            u'IOpportunity not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('opportunity', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('opportunity', parent.objectIds())

    def test_ct_opportunity_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Opportunity')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_opportunity_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Opportunity')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'opportunity_id',
            title='Opportunity container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
