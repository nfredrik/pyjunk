from jsonplaceholder import REST

@given(u'I am using the client trying to setup a conversation with a rest service using some resources')
def step_impl(context):
    context.rest = REST()
    assert context.rest is not None 

@given(u'I ask for supported operations on a resource')
def step_impl(context):
    context.tmp = context.rest.show_primitives().options()
 

@then(u'I will get a reply on supported operations')
def step_impl(context):
    ll = set(context.tmp.split(','))
    at_least = set(['PUT', 'GET'])
    assert at_least.issubset(ll)
    #raise NotImplementedError(u'STEP: Then I will get a reply on supported operations')

@given(u'I want to retrieve the information about resource "1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource "1"')

@then(u'I should see json information about resource "1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see json information about resource "1"')

@given(u'I want to retrieve the information about resource 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource 1')

@then(u'I should see json information about resource <1>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see json information about resource <1>')

@given(u'I input "<addent1>" add "<addent2>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I input "<addent1>" add "<addent2>"')

@then(u'I should see "<result>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "<result>"')

@given(u'I want to retrieve the information about resource 45')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource 45')

@given(u'I want to retrieve the information about resource 100')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource 100')

@given(u'I want to retrieve the information about resource 501')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource 501')

@given(u'I want to retrieve the information about all resources')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about all resources')

@then(u'I should see a list of json information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see a list of json information')