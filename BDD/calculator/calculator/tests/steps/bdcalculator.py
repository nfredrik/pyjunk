from hamcrest import assert_that, equal_to, is_not
@given(u'I am using the calculator')
def step_impl(context):
    if hasattr(context, "calc"):
       assert_that(context.calc, is_not(equal_to(None)))
 

#@given(u'I input "2" add "2"')
@given(u'I input "{addent1}" add "{addent2}"')
def step_impl(context, addent1, addent2):
    context.result = context.calc.add(int(addent1), int(addent2))

@then(u'I should see "{expected_result}"')
def step_impl(context, expected_result):
    assert_that(int(expected_result), equal_to(context.result))