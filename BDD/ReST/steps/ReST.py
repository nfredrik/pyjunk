import json
#import validictory
#import jsonvalidate
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
      "type": "string"
    }
 
  }


def is_valid_json(text):
    try:
        json.dumps(text)
        return True
    except:
        return False

def assert_valid_dict(dict):
    for key in ['id', 'body', 'title', 'userId']:
        if key not in dict.keys():
            raise failureException("%s not in dict"%key)

        if dict[key] is None:
            raise failureException("no value for %s"%key)

    #validate_json(str(dict))

def assert_valid_list(list):
    for dict in list:
        assert_valid_dict(dict)


@given(u'I am using the client trying to setup a conversation with a rest service using some resources')
def step_impl(context):
    context.rest = REST()
    assert context.rest is not None 

@given(u'I ask for supported methods on a resource')
def step_impl(context):
    context.tmp = context.rest.show_primitives().options()
 

@then(u'I will get a reply on supported methods')
def step_impl(context):
    ll = set(context.tmp.split(','))
    print('Supported HTTP methods', ll)
    at_least = set(['PUT', 'GET'])
    assert at_least.issubset(ll)
    #raise NotImplementedError(u'STEP: Then I will get a reply on supported methods')

@given(u'I want to retrieve the information about resource "{resource_no}"')
def step_impl(context, resource_no):
    context.tmp = context.rest.show_resource(number=resource_no).json
    assert context.tmp is not None

@then(u'I should see json information about resource "{resource_no}"')
def step_impl(context, resource_no):
    # Check if json
    assert isinstance(context.tmp,dict)
    assert is_valid_json(context.tmp)
    jonne = json.dumps(context.tmp)
    #print('Mer:',jonne)
    #validictory.validate(jonne, schema)
    #jsonvalidate.validate(jonne, schema, [], None)

    assert_that(str(context.tmp['id']), equal_to(resource_no))


@given(u'I want to retrieve the information about all resources')
def step_impl(context):
    context.tmp = context.rest.list_resources().json
    assert context.tmp is not None
 
@then(u'I should see a list of json information')
def step_impl(context):
        assert_that(type(context.tmp), equal_to(list))
        assert_valid_list(context.tmp)


@given(u'I try to retrieve a non existing resource')
def step_impl(context):
    context.tmp = context.rest.show_resource(number='501').json
    assert context.tmp is not None

@then(u'It throws a KeyError exception')
def step_impl(context):
    try:
        context.tmp['id']
        assert False
    except KeyError as e:
        assert True

