from behave import *
from hamcrest import *
import re
import pprint
use_step_matcher("re")

# Nice page about behave!
# http://jenisys.github.io/behave.example/tutorials/tutorial04.html

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
    validate_in_h1(context, context.subject)

@then(u'I find relevant information')
def step_impl(context):
    validate_relevance_for(context,context.subject)

def search_for(context, subject):
    elem = context.browser.find_element_by_id("searchInput")
    elem.send_keys(subject)
    elem.send_keys(context.Keys.RETURN)
    #elem.clear()

def validate_relevance_for(context,subject):
    assert isinstance(subject, str), "{}".format(type(subject))
    subject = dequote(subject)

    check = {"Capybara": "is the largest rodent in the world", 
              "Selenium": "reduce the effects of mercury toxicity"}

    result = check.get(subject,"Fredrik Svard")

    assert subject in context.browser.page_source,"{}".format(subject)
    assert result in context.browser.page_source, "{} {}".format(result, subject)


def validate_in_h1(context, subject):

    lst = context.browser.find_elements_by_tag_name('h1') 
    subject = dequote(subject)
    for l in lst:       
        if subject == l.text:
            return             # We have a match!

    assert False


def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

