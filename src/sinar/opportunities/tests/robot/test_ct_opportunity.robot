# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.opportunities -t test_opportunity.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.opportunities.testing.SINAR_OPPORTUNITIES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/opportunities/tests/robot/test_opportunity.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Opportunity
  Given a logged-in site administrator
    and an add Opportunity form
   When I type 'My Opportunity' into the title field
    and I submit the form
   Then a Opportunity with the title 'My Opportunity' has been created

Scenario: As a site administrator I can view a Opportunity
  Given a logged-in site administrator
    and a Opportunity 'My Opportunity'
   When I go to the Opportunity view
   Then I can see the Opportunity title 'My Opportunity'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Opportunity form
  Go To  ${PLONE_URL}/++add++Opportunity

a Opportunity 'My Opportunity'
  Create content  type=Opportunity  id=my-opportunity  title=My Opportunity

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Opportunity view
  Go To  ${PLONE_URL}/my-opportunity
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Opportunity with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Opportunity title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
