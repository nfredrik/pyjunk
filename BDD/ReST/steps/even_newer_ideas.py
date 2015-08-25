from namedhttpstatus import NamedHTTPstatus

# Given - Setup, put in to context, prepare
# When  - Commit, release, let loose, do the intended thing
# Then  - Check/Verify the outcome

# Me want to request a post resource with an id of 7
@given(u'Me want to interact with a {typ} resource {xid} {no}')
def step_impl(context, typ, xid, no):
    context.CustomWorld.set_resource_type(typ)
    print("Help", xid, no)
    context.CustomWorld.set_substitution('{'+xid+'}',no)

@when(u'I request it')
def step_impl(context):
    nisse = context.CustomWorld.request_resource()
    assert nisse is not None

@then(u'I will get it')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("OK"))