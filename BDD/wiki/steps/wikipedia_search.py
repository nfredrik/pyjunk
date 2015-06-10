from behave import *
import html5lib
use_step_matcher("re")

# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
#
#  TODO
#  - How to remember values btw features?
#
#
#

@given('I can access Wikipedia')
def step_impl(context):
    context.browser.get('http://en.wikipedia.org/wiki/Main_Page')
    assert "Wikipedia" in context.browser.title

@when(u'I search for "(?P<text>.*)"')
def step_impl(context, text):
    search_for(context, text)

@then(u'I get a result for "(?P<text>.*)"')
def step_impl(context, text):
    assert text in context.browser.page_source

#@when(u'I search for (?P<text>.*)')
@when(u'I search for (?P<text>[\w]+)')
def step_impl(context, text):
    context.execute_steps(u'''When I search for "{}"'''.format(text))
 
@then(u'I get a result for (?P<text>.*)')
def step_impl(context, text):
    context.execute_steps(u'''Then I get a result for "{}"'''.format(text))

@when(u'I search for the subject (?P<text>.*)')
def step_impl(context, text):
    context.execute_steps(u'''When I search for "{}"'''.format(text))
    context.subject = text

@then(u'I find relevant information on (?P<text>.*)')
def step_impl(context, text):
    validate_relevance_for(context, text)

@then(u'I get a matching result')
def step_impl(context):
#   expect(find('h1').text).to eq(@subject)
    assert context.subject in context.browser.page_source
    pass

@then(u'I find relevant information')
def step_impl(context):
    validate_relevance_for(context,context.subject)

def search_for(context, subject):
    elem = context.browser.find_element_by_id("searchInput")
    elem.send_keys(subject)
    elem.send_keys(context.Keys.RETURN)

def validate_relevance_for(context,subject):
    assert subject in context.browser.page_source,"{}".format(subject)
    #assert 'is the largest rodent in the world' in context.browser.page_source


