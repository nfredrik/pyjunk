from namedhttpstatus import NamedHTTPstatus

#  behave --tags=test --no-capture

@given(u'the server knows about the following resources')
def step_impl(context):
    context.CustomWorld.set_resources(context.table)

@given(u'the server knows about the following mime types')
def step_impl(context):
    context.CustomWorld.set_mime_types(context.table)

@given(u'I want to interact with an {resource} resource')
def step_impl(context, resource):
    context.CustomWorld.set_resource_type(resource)

@then(u'I can request it')
def step_impl(context):
    nisse = context.CustomWorld.request_resource()
    assert nisse is not None


@given(u'I want to request a {res} resource with an {xid} of {no}')
def step_impl(context, res, xid, no):
    context.CustomWorld.set_resource_type(res)
    print('xid', xid, 'no', no)
    context.CustomWorld.set_substitution('{'+xid+'}',no)
    nisse = context.CustomWorld.request_resource()
    assert nisse is not None

@given(u'the request succeeds')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("OK"))

@given(u'the create succeeds')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("CREATED"))

@then(u'I can read it\'s content')
def step_impl(context):
    context.CustomWorld.assert_have_content()



@given(u'the server knows the structure of the payload')
def step_impl(context):
    context.CustomWorld.set_payloads(context.table)


@given(u'I want to create a {res} resource with an {xid} of {no} and payload {payloadid}')
def step_impl(context, res, xid, no, payloadid):
    context.CustomWorld.set_resource_type(res)
    context.CustomWorld.set_substitution('{'+xid+'}',no)
    context.CustomWorld.set_payload(payloadid)
    nisse = context.CustomWorld.create_resource()
    assert nisse is not None

@then(u'I can verify the reply')
def step_impl(context):
    context.CustomWorld.assert_have_content()

@then(u'the request succeeds')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("OK"))

@then(u'the response type is {Cj}')
def step_impl(context, Cj):
    context.CustomWorld.assert_mime_type(Cj)    


@then(u'the Cj response has a {name} link')
def step_impl(context, name):
    context.CustomWorld.assert_attribute(name)

@then(u'I can find the id from the link response')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can find the id from the link response')


@then(u'I can request a the {name} link')
def step_impl(context, name):
    context.CustomWorld.request_resource_ng()

@then(u'I can find the {attr} from the link response')
def step_impl(context, attr):
    context.CustomWorld.assert_mime_type('png')
    #context.CustomWorld.assert_attribute_in_text("viewport")






