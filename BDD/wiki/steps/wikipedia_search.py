from behave import given, when, then
use_step_matcher("re")

# Nice page about behave!
# http://jenisys.github.io/behave.example/tutorials/tutorial04.html
#
# TODO:
#       - better than this? : context.browser.page_source  -No, move perhaps?
#       - Possible to leave out context as paramenter? 



@given('I can access Wikipedia')
def step_impl(context):

    #assert context.failed is False   # santity check  How is it used????
    
    context.browser.get('http://en.wikipedia.org/wiki/Main_Page')
    assert "Wikipedia" in context.browser.title


@when(u'I search for "(?P<text>.*)"')
def step_impl(context, text):
    search_for(context, text)


@then(u'I get a result for "(?P<text>.*)"')
def step_impl(context, text):
    assertIn(text,context)


@when(u'I search for (?P<text>[\w]+)')
def step_impl(context, text):
    search_for(context, text)


@then(u'I get a result for (?P<text>.*)')
def step_impl(context, text):
    # Check if calling internal works ...
    context.execute_steps(u'''Then I get a result for "{}"'''.format(text))


@when(u'I search for the subject "(?P<text>.*)"')
def step_impl(context, text):
    search_for(context, text)
    # Save for later use
    context.subject = text


@then(u'I find relevant information on (?P<text>.*)')
def step_impl(context, text):
    validate_relevance_for(context, text)


@then(u'I get a matching result')
def step_impl(context):
    validate_subject_in_h1(context, context.subject)


@then(u'I find relevant information')
def step_impl(context):
    validate_relevance_for(context, context.subject)

#
# Helper functions
#
def assertIn(input, context):                  # Better name!
    assert input in context.browser.page_source

def search_for(context, subject):
    elem = context.browser.find_element_by_id("searchInput")
    elem.send_keys(subject)
    elem.send_keys(context.Keys.RETURN)


def validate_relevance_for(context, subject):

    check = {"Capybara": "is the largest rodent in the world",
             "Selenium": "reduce the effects of mercury toxicity"}
    result = check.get(subject, "This is an error!")

    assertIn(result, context)


def validate_subject_in_h1(context, subject):

    lst = context.browser.find_elements_by_tag_name('h1')

    if any([subject == l.text  for l in lst]):
        return

    assert False
