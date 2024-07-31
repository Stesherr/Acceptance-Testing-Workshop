from behave import *
from task import Task


@given("the list has five elements")
def step_impl(context):
    global listT 
    listT = list([])
    listT.append(Task("eat"))
    listT.append(Task("study"))
    listT.append(Task("travel"))
    listT.append(Task("edit"))
    listT.append(Task("walk"))

@when('the user selects option "{option}"')
def  step_impl(context, option):
    assert option == "5"


@when('the user chooses task "{option}"')
def  step_impl(context, option):
    assert option == "2"


@when('the user enters the name "{name}"')
def  step_impl(context, name):
    assert name == "program"

@then('the task in "{option}" has the name "{name}"')
def step_impl(context, option, name):
    listT[int(option)-1].setname(name)
    #assert listT[option-1] == name, f'task in"{option}" no change'