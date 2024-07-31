from behave import *
from task import Task


@given("the list has at least one element")
def step_impl(context):
    global listT 
    listT = list([])
    listT.append(Task("eat"))
    listT.append(Task("study"))


@when('the user chooses option "{option}"')
def  step_impl(context, option):
    assert option == "2"


@then('the list size is greater than zero')
def step_impl(context):
    assert len(listT)>0