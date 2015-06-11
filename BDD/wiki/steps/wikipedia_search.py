from behave import *
from hamcrest import *
import re
import pprint
use_step_matcher("re")

# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
#
#  TODO
#  - How to remember values btw features?, implemented!!
#  - How to find a subject inside a html tag like <h1> ... </h1>
#  - How to match a subject in a dictonary and get a value to match against a .text?
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
    # assert context.subject in context.browser.page_source
    # assert context.subject
    # assert context.browser.page_source
    # assert isinstance(context.browser.find_elements_by_tag_name('h1'), list)
    # #assert context.subject in context.browser.find_elements_by_tag_name('h1')

    # pp = pprint.PrettyPrinter(indent=4)
    # jj = context.browser.find_elements_by_tag_name('h1') 
    # for j in jj:
    #     #print(dir(j))
    #     print(j.text)
    #     print(j.id)
        #assert context.subject in j, "{} {}".format(context.subject, j)

    validate_in_h1(context, context.subject)

@then(u'I find relevant information')
def step_impl(context):
    validate_relevance_for(context,context.subject)

def search_for(context, subject):
    elem = context.browser.find_element_by_id("searchInput")
    elem.send_keys(subject)
    elem.send_keys(context.Keys.RETURN)
    #elem.clear()

def old_validate_relevance_for(context,subject):
    assert subject in context.browser.page_source,"{}".format(subject)
    #assert 'is the largest rodent in the world' in context.browser.page_source

def validate_relevance_for(context,subject):
    assert isinstance(subject, str), "{}".format(type(subject))
    #subject.replace('"','')
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
#        print('Compare:{} with {}'.format(subject, l.text))
        if subject == l.text:
#            print("return from validate_in_h1")
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

