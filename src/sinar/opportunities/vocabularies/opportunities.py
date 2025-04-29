# -*- coding: utf-8 -*-

# from plone import api
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer
from sinar.opportunities import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class Opportunities(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [

            # Invitations for NGOs, civil society groups, or tech
            # developers to collaborate on projects, initiatives, or
            # campaigns.
            VocabItem('coalitions', _('Coalition Building, \
                                      Call for Partnerships and Joint Campaigns')),

            # Invitations to submit project proposals or bid for
            # consultancy or service contracts, often issued by NGOs,
            # governments, or international organizations
            VocabItem('cfp', _('Call for Proposals / Tenders')),

            # Tech competitions, hackathons, innovation challenges, or
            # calls for project submissions offering prizes or
            # recognition
            VocabItem('competitions', _('Competitions')),

            # Open calls for participation, speaking engagements, or
            # registrations for civic tech, human rights, digital
            # innovation conferences or forums
            VocabItem('events', _('Event Participation/Call for Sessions')),

            # Competitive programs offering individuals financial
            # support, mentorship, and project development resources,
            # often for advocacy, research, leadership, or tech
            # innovation
            VocabItem('fellowships', _('Fellowships')),

            # Short-term work experiences intended for skills-building
            # and civic contribution
            VocabItem('internships', _('Internships')),

            # Open employment positions at NGOs, civic tech
            # organizations, public interest tech groups, or related
            # sectors.
            VocabItem('jobs', _('Jobs')),


            # Financial aid opportunities for formal education
            # (undergraduate, graduate, certifications) related to
            # technology, governance, journalism, or human rights.
            VocabItem('scholarships', _('Scholarships')),

            # Volunteer programs, or unpaid roles intended for
            # skills-building and civic contribution
            VocabItem('voluteering', _('Volunteering')),

            # Learning opportunities including workshops, bootcamps, training series,
            # or short courses on civic tech, governance, digital security, open data,
            # or related topics.
            VocabItem('workshops', _('Training and Workshops')),

        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


OpportunitiesFactory = Opportunities()
