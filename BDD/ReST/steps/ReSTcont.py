import json
import requests
from hamcrest import assert_that, contains_string, equal_to, is_not, not_none, less_than, less_than_or_equal_to 
from jsonplaceholder import REST
from namedhttpstatus import NamedHTTPstatus
import datetime
from dateutil import parser

@given(u'I order to create a new resource "{resource}"')
def step_impl(context, resource):    
    data = json.dumps({"title":"foo", "body":"bar", "userId":"1"})
    context.j, context.payload = context.rest.create_resource().create(data)
    #assert context.text is not None

@then(u'get an "{status_code}" in the reply')
def step_impl(context, status_code):
    assert_that(context.j.status_code, equal_to(NamedHTTPstatus.from_string(status_code)))

@then(u'I will get a confirmation that resource "{resource:d}" has been created')
def step_impl(context, resource):
    expect = {"id":101, "title":"foo", "body":"bar", "userId": resource} # TODO Check if this could be done earlier!
    text = json.loads(context.payload)
    assert_that(text, equal_to(expect))

@given(u'I order to delete resource "{resource}"')
def step_impl(context, resource):
    context.j = context.rest.delete_resource(number=resource).delete()

@given(u'I order a partial update of resource "{resource}"')
def step_impl(context, resource):
    data = {'title':'foo', 'body':'bar', 'userId':resource}
    context.j, context.payload = context.rest.patch_resource(number=resource).patch(data)

@then(u'some information in return')
def step_impl(context):
    assert_that(context.payload, not_none())


@given(u'I want to know if "{resource}" exists as a resource')
def step_impl(context, resource):
    context.j, context.time = context.rest.head_resource(number=resource).head()
    assert context.j is not None


@then(u'I will get metadata as reply')
def step_impl(context):
    actual_time = parser.parse(context.time)
    assert_that(actual_time, less_than_or_equal_to(datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)))

@given(u'I order to update resource "{resource}"')
def step_impl(context, resource):
    data = json.dumps({'title':'foo', 'body':'bar', 'userId':'1'})     
    context.j, context.tmp = context.rest.update_resource(number=resource).update(data)

# https://pythonhosted.org/behave/parse_builtin_types.html

@then(u'I will get a confirmation that resource "{resource:d}" has been updated')
def step_impl(context, resource):
    assert_that(context.tmp, not_none())

    expect = {"id":1, "title":"foo", "body":"bar" }
    expect["userId"] = resource  # TODO Check if this could be done earlier!
    #assert context.text is not None
    text = json.loads(context.tmp)
    assert_that(text, equal_to(expect))








