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

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(IOpportunityDeadline)
@adapter(IOpportunityDeadlineMarker)
class OpportunityDeadline(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if safe_hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value
