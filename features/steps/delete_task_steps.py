from behave import *
from task import Task


@given("the list has one or more elements")
def step_impl(context):
    global listT
    listT = list([])
    listT.append(Task("eat"))
    listT.append(Task("study"))


@when('the user picks up option "{option}"')
def  step_impl(context, option):
    assert option == "4"


@then('the size of the list is zero')
def step_impl(context):
    listT.clear()
    assert len(listT)==0