import json
import validictory
from hamcrest import assert_that, contains_string, equal_to, is_not
from jsonplaceholder import REST

schema={
    "id": {
      "type": "integer"
    },
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "userId": {
      "type": "integer"
    }
  }


def is_valid_json(text):
    try:
        json.dumps(text)
        return True
    except:
        return False


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

@given(u'I want to retrieve the information about resource "{resource_no}"')
def step_impl(context, resource_no):
    context.tmp = context.rest.show_resource(number=resource_no).json
    assert context.rest is not None

@then(u'I should see json information about resource "{resource_no}"')
def step_impl(context, resource_no):
    # Check if json
    assert isinstance(context.tmp,dict)
    assert is_valid_json(context.tmp)
    data = json.dumps(context.tmp)
    validictory.validate(data, schema)
    print('Mer:',context.tmp['id'])
    assert_that(str(context.tmp['id']), equal_to(resource_no))
    #assert False

@given(u'I want to retrieve the information about resource 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I want to retrieve the information about resource 1')

@then(u'I should see json information about resource <1>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see json information about resource <1>')

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