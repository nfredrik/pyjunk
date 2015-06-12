from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to, is_not
use_step_matcher("re")

# Check
# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
# https://github.com/hamcrest/PyHamcrest

@given('I can access Wikipedia')
def step_impl(context):

    context.browser.get('http://en.wikipedia.org/wiki/Main_Page')
    assert_that(context.browser.title, contains_string("Wikipedia"))

    helper = getattr(context, "helper", None)

    if not helper:
        context.helper = Helper(context)


@when(u'I search for "(?P<text>.*)"')
def step_impl(context, text):
    context.helper.search_for(text)


@then(u'I get a result for "(?P<text>.*)"')
def step_impl(context, text):
    context.helper.assert_in_page(text)


@when(u'I search for (?P<text>[\w]+)')
def step_impl(context, text):
    context.helper.search_for(text)


@then(u'I get a result for (?P<text>.*)')
def step_impl(context, text):
    # Check if calling internal works ...
    context.execute_steps(u'''Then I get a result for "{}"'''.format(text))


@when(u'I search for the subject "(?P<text>.*)"')
def step_impl(context, text):
    context.subject = text # Save for later use
    context.helper.search_for(text)



@then(u'I find relevant information on (?P<text>.*)')
def step_impl(context, text):
    context.helper.validate_relevance_for(text)


@then(u'I get a matching result')
def step_impl(context):
    context.helper.validate_subject_in_h1(context.subject)


@then(u'I find relevant information')
def step_impl(context):
    context.helper.validate_relevance_for(context.subject)

#
# Helper class
#
class Helper():
    check = {"Capybara": "is the largest rodent in the world",
             "Selenium": "reduce the effects of mercury toxicity"}

    def __init__(self, context= None):
        self.context = context

    def assert_in_page(self, input):
        assert_that(self.context.browser.page_source, contains_string(input))

    def search_for(self, subject):
        elem = self.context.browser.find_element_by_id("searchInput")
        elem.send_keys(subject)
        elem.send_keys(self.context.Keys.RETURN)

    def validate_relevance_for(self, subject):
     
        result = self.check.get(subject, "This is an error!")

        self.assert_in_page(result)

    def validate_subject_in_h1(self, subject):

        lst = self.context.browser.find_elements_by_tag_name('h1')

        if any([subject == l.text  for l in lst]):
            return

        assert_that(False)
