from namedhttpstatus import NamedHTTPstatus

# TODO:
# type checking in all steps, http://jenisys.github.io/behave.example/datatype/builtin_types.html
# Get it right with "Given,When,Then-concept", start small
# Introduce validation of json format


# Given - Setup, put in to context, prepare
# When  - Commit, release, let loose, do the intended thing
# Then  - Check/Verify the outcome

# Me want to request a post resource with an id of 7
@given(u'Me want to interact with a {typ:w} resource with an {xid:w} of {no:w}')
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


@then(u'can verify the content')
def step_impl(context):
    # Verify the content according to a json schema. Is this possible?
    context.CustomWorld.assert_have_content()
    context.CustomWorld.assert_valid_payload()

@when(u'I delete it')
def step_impl(context):
    context.CustomWorld.delete_resource()

@then(u'I get a delete confirmation')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("NO_CONTENT"))


    


@given(u'I want to know supported methods')
def step_impl(context):
    # Really no setup or similar just continue
    pass

@when(u'I ask for it')
def step_impl(context):
    context.CustomWorld.supported_methods()

@then(u'I will get it as metadata')
def step_impl(context):
    context.CustomWorld.assert_response(NamedHTTPstatus.from_string("NO_CONTENT"))

@then(u'It will be set or subset of the RestAPI')
def step_impl(context):
    context.CustomWorld.assert_supported_methods(set(['PUT', 'GET']))


@when(u'Check for it\'s existance')
def step_impl(context):
    context.CustomWorld.check_for_existence()

@then(u'check that the metadata is valid')
def step_impl(context):
    context.CustomWorld.assert_valid_metadata()


