import os
import sys
from hamcrest import assert_that, is_
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from util.utils import get, post, delete, put, generate_data_file


@step(u'I register an user with email "{email}" and "{password}"')
def step_impl(context, email, password):
    data = generate_data_file(email=email, password=password)
    context.response = post(context.base_url + "register", data=data)


@step(u'I register an user with email folowing data')
def step_impl(context ):
    for row in context.table:
        data = generate_data_file(email=row['email'], password=row['password'])
        context.response = post(context.base_url + "register", data=data)


@step(u'I login with email "{email}" and "{password}"')
def step_impl(context, email, password):
    data = generate_data_file(email=email, password=password)
    context.response = post(context.base_url + "login", data=data)
    context.token = context.response.json()['token']


@step(u'I login only with email "{email}"')
def step_impl(context, email):
    data = generate_data_file(email=email)
    context.response = post(context.base_url + "login", data=data)


@step(u'I register an employee with name "{name}" and job "{job}"')
def step_impl(context, name, job):
    data = generate_data_file(name=name, job=job)
    context.response = post(context.base_url + "users", token=context.token, data=data)


@step(u'I register an employee with name {name} and job {job}')
def step_impl(context, name, job):
    data = generate_data_file(name=name, job=job)
    context.response = post(context.base_url + "users", context.token, data)


@step(u'I change an employee {employee_id} with name "{name}" and job "{job}"')
def step_impl(context, employee_id, name, job):
    data = generate_data_file(name=name, job=job)
    context.response = put(context.base_url + "users/" + employee_id, token=context.token, data=data)


@step(u'I delete the employee {employee_id}')
def step_impl(context, employee_id):
    context.response = delete(context.base_url + "users/" + employee_id, token=context.token)


@step(u'I search the employee {employee_id}')
def step_impl(context, employee_id):
    context.response = get(context.base_url + "users/" + employee_id, token=context.token)


@step(u'I get employee list with page {page}')
def step_impl(context, page):
    context.response = get(context.base_url + "users", token=context.token, page=page)


@then(u'I verify that status code is "{status_code}"')
def step_impl(context, status_code):
    assert_that(context.response.status_code, is_(int(status_code)))


@step(u'I prepare environment for tests run')
def step_impl(context):
    context.execute_steps('''
        Given I register an user with email "mauricio.chaves.junior" and "123456"
        And I login with email "mauricio.chaves.junior" and "123456"
    ''')