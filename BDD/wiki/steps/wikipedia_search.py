from behave import *
from hamcrest import *
from html.parser import HTMLParser
import re
use_step_matcher("re")

# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
#
#  TODO
#  - How to remember values btw features?
#
#
#
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)


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
    parser = MyHTMLParser()
    print(parser.feed(context.browser.page_source))

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
    assert context.subject
    assert context.browser.page_source
    # validate_in_h1(context.browser.page_source, context.subject)

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

def assertFalse():
    assert False

def new_validate_relevance_for(context,subject):
    assert isinstance(subject, str), "{}".format(type(subject))
    subject.replace('"','')

    check = {"Capybara": "is the largest rodent in the world", 
              "Selenium": "reduce the effects of mercury toxicity"}

    result = check.get(subject,"Fredrik Svard")

    assert subject in context.browser.page_source,"{}".format(subject)
    assert result in context.browser.page_source, "{} {}".format(result, subject)

def validate_in_h1(page, subject):

    match = re.findall(r'<h1>.*</h1>', page)

    assert match

    for i in match:
        print(i)
        if subject == i:
            return

    assert False

