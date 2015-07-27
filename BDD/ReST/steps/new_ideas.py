#resources = dict()

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
    context.CustomWorld.set_substitution([xid,no])
    nisse = context.CustomWorld.request_resource()
    assert nisse is not None

@given(u'the request succeeds')
def step_impl(context):
    context.CustomWorld.assert_response(200)

@then(u'I can read it\'s content')
def step_impl(context):
    context.CustomWorld.assert_have_content(True)


