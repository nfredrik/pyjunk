
# https://gist.github.com/pazdera/1173009
# https://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge#Python

# Try to avoid checking if Linux or Windows. Use duck typing, if exception thrown, check next implementation

@given(u'That current directory is "."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given That current directory is "."')

@then(u'Verify that at least one file is listed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify that at least one file is listed')

@then(u'We have a parent directory')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then We have a parent directory')

@given(u'That we have a network interface')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given That we have a network interface')

@then(u'Verify that we have MAC')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify that we have MAC')

@then(u'Ping on own local IP-address')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Ping on own local IP-address')