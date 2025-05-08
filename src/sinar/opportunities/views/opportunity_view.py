# -*- coding: utf-8 -*-

# from sinar.opportunities import _
from zope.publisher.browser import BrowserView
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IOpportunityView(Interface):
    """ Marker Interface for IOpportunityView"""


@implementer(IOpportunityView)
class OpportunityView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('opportunity_view.pt')

    def opportunity_type_titles(self):

        factory = getUtility(IVocabularyFactory,
                             'sinar.opportunities.opportunity_types')

        vocabulary = factory(self)
        if self.context.opportunity_types:
            titles = []
            for opportunity_type in self.context.opportunity_types:
                term = vocabulary.getTerm(opportunity_type)
                titles.append(term.title)
            return titles

    def __call__(self):
        # Implement your own actions:
        return self.index()
