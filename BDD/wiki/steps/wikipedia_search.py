from behave import given, when, then

@given('I can access Wikipedia')
def step_impl(context):
    context.browser.get('http://en.wikipedia.org/wiki/Main_Page')

# "(.*)"
@when(u'I search for "{text}"')
#@when(u'I search for "(?P<text>".*")"')
def step_impl(context, text):
    context.browser.get('http://en.wikipedia.org/wiki/Main_Page') 
    assert "Wikipedia" in context.browser.title
    #print('conext browser:{}'.format(vars(context.browser)))
    elem = context.browser.find_element_by_id("searchInput")
    elem.send_keys(text)
    elem.send_keys(context.Keys.RETURN)
    assert True

@then(u'I get a result for "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source

# http://jenisys.github.io/behave.example/tutorials/tutorial04.html

@when(u'When I search for {subject}')
def step_impl(context):
    for row in context.table:
        print(row['subject'])
    # raise NotImplementedError(u'STEP: When I search for Capybara')

# @then(u'I get a result for Capybara')
# def step_impl(context):
#     pass
    #raise NotImplementedError(u'STEP: Then I get a result for Capybara')

# @then(u'I find relevant information on Capybara')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I find relevant information on Capybara')

# @when(u'I search for Selenium')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I search for Selenium')

# @then(u'I get a result for Selenium')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I get a result for Selenium')

# @then(u'I find relevant information on Selenium')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I find relevant information on Selenium')

# @when(u'I search for the subject "Capybara"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I search for the subject "Capybara"')

# @then(u'I get a matching result')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I get a matching result')

# @then(u'I find relevant information')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I find relevant information')

# @when(u'I search for the subject "Selenium"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I search for the subject "Selenium"') 