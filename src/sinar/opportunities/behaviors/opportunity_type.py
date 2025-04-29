# -*- coding: utf-8 -*-

from sinar.opportunities import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IOpportunityTypesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IOpportunityTypes(model.Schema):
    """
    """

    directives.widget(opportunity_types=SelectFieldWidget)
    opportunity_types = schema.List(
        title='Opportunity Types',
        description='Select opportunity types that best fit this'
                    + 'announceement.',
        value_type=schema.Choice(
            vocabulary='sinar.opportunities.opportunity_types',),
        required=True,
    )


@implementer(IOpportunityTypes)
@adapter(IOpportunityTypesMarker)
class OpportunityTypes(object):
    def __init__(self, context):
        self.context = context

    @property
    def opportunity_types(self):
        if safe_hasattr(self.context, 'opportunity_types'):
            return self.context.opportunity_types
        return None

    @opportunity_types.setter
    def opportunity_types(self, value):
        self.context.opportunity_types = value
