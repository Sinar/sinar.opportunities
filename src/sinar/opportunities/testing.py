# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.opportunities


class SinarOpportunitiesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.opportunities)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.opportunities:default')


SINAR_OPPORTUNITIES_FIXTURE = SinarOpportunitiesLayer()


SINAR_OPPORTUNITIES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_OPPORTUNITIES_FIXTURE,),
    name='SinarOpportunitiesLayer:IntegrationTesting',
)


SINAR_OPPORTUNITIES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_OPPORTUNITIES_FIXTURE,),
    name='SinarOpportunitiesLayer:FunctionalTesting',
)


SINAR_OPPORTUNITIES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_OPPORTUNITIES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarOpportunitiesLayer:AcceptanceTesting',
)
