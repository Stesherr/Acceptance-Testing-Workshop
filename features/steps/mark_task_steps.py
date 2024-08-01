from behave import *
from task import Task

def isOnList(task, listTask):
    for value in listTask:
        if(value.getName() == task.getName()):
            return True
    return False


@given("the list has four elements")
def step_impl(context):
    global listT
    listT = list([])
    listT.append(Task("run"))
    listT.append(Task("eat"))
    listT.append(Task("jump"))
    listT.append(Task("draw"))


@when('the user takes option "{option}"')
def step_impl(context, option):
    assert option == "3"


@when('the user chooses task "{option}"')
def step_impl(context, option):
    assert option == "2"


@then('the list no longer contains task "{numTask}"')
def step_impl(context, numTask):
    task = listT.pop(int(numTask))
    assert isOnList(task, listT) == False, f'Task "{task}" not on to-do list'