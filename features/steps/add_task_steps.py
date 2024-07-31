from behave import *
from task import Task

def isOnList(task, listTask):
    for value in listTask:
        if(value.getNombre() == task.getNombre()):
            return True
    return False


@given("list is empty")
def step_impl(context):
    global list
    list = []


@when('the user enters the task "{task}"')
def step_impl(context, task):
    list.append(Task(task))


@then('la lista debe contener "{task}"')
def step_impl(context, task):
    assert isOnList(Task(task), list), f'Task "{task}" is not on the to-do list'