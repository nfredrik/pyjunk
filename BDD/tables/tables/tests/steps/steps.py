from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not
from company_model import CompanyModel
from testutil import NamedNumber

@given('a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel()

    for row in context.table:
        context.model.add_user(name=row["name"], department=row["department"])
    assert True

@when(u'we count the number of people in the department')
def step_impl(context):
    context.model.count_persons_per_department()

@then(u'we will find {count} people in "{department}"')
def step_impl(context, count, department):
    count_ = NamedNumber.from_string(count)
    assert_that(count_, equal_to(context.model.get_headcount_for(department)))

@then(u'we find "{count}" person in "{department}"')
def step_impl(context, count, department):
    assert_that(NamedNumber.from_string(count), equal_to(context.model.get_headcount_for(department)))
    #assert context.model.get_headcount_for(department) == NamedNumber.from_string('one')