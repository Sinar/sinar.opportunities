# -*- coding: utf-8 -*-

from sinar.opportunities import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IOpportunityDeadlineMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IOpportunityDeadline(model.Schema):
    """
    """

    opportunity_open = schema.Date(
        title=_('Open Date'),
        description=_('Opportunity Open Date'),
        required=False,
    )

    opportunity_close = schema.Date(
        title=_('Closing Date'),
        description=_('Opportunity Closing Date or Deadline'),
        required=False,
    )


@implementer(IOpportunityDeadline)
@adapter(IOpportunityDeadlineMarker)
class OpportunityDeadline(object):
    def __init__(self, context):
        self.context = context

    @property
    def opportunity_open(self):
        if safe_hasattr(self.context, 'opportunity_open'):
            return self.context.opportunity_open
        return None

    @opportunity_open.setter
    def opportunity_open(self, value):
        self.context.opportunity_open = value

    @property
    def opportunity_close(self):
        if safe_hasattr(self.context, 'opportunity_close'):
            return self.context.opportunity_close
        return None

    @opportunity_close.setter
    def opportunity_close(self, value):
        self.context.opportunity_close = value
