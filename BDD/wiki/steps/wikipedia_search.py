from behave import given, when, then
use_step_matcher("re")

# Nice page about behave!
# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
#
# TODO:
#       - better than this? : context.browser.page_source  -No, move perhaps?


@given('I can access Wikipedia')
def step_impl(context):

    #assert context.failed is False   # santity check  How is it used????
    
    context.browser.get('http://en.wikipedia.org/wiki/Main_Page')
    assert "Wikipedia" in context.browser.title

    helper = getattr(context, "helper", None)

    if not helper:
        context.helper = Helper(context)


@when(u'I search for "(?P<text>.*)"')
def step_impl(context, text):
    context.helper.search_for(text)


@then(u'I get a result for "(?P<text>.*)"')
def step_impl(context, text):
    context.helper.assertIn(text)


@when(u'I search for (?P<text>[\w]+)')
def step_impl(context, text):
    context.helper.search_for(text)


@then(u'I get a result for (?P<text>.*)')
def step_impl(context, text):
    # Check if calling internal works ...
    context.execute_steps(u'''Then I get a result for "{}"'''.format(text))


@when(u'I search for the subject "(?P<text>.*)"')
def step_impl(context, text):
    context.helper.search_for(text)
    # Save for later use
    context.subject = text


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

    def __init__(self, context = None):
        self.context = context

    def assertIn(self, input):                  # Better name!
        assert input in self.context.browser.page_source

    def search_for(self, subject):
        elem = self.context.browser.find_element_by_id("searchInput")
        elem.send_keys(subject)
        elem.send_keys(self.context.Keys.RETURN)

    #@classmethod
    def validate_relevance_for(self, subject):
     
        result = self.check.get(subject, "This is an error!")

        self.assertIn(result)


    def validate_subject_in_h1(self, subject):

        lst = self.context.browser.find_elements_by_tag_name('h1')

        if any([subject == l.text  for l in lst]):
            return

        assert False
