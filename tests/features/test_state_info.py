import pytest
import requests
from pytest_bdd import scenarios, when, then

API = "http://localhost:5000/"
scenarios('state_info.feature', example_converters=dict(search=str, name=str, capital=str, statehood=str, timezones=str))


@pytest.fixture
@when('the API is queried for "<search>"')
def call_response(search):
    param = {'format':'json'}
    response = requests.get(API + "?search=" + search, params=param)
    return response


@then('the name and abbreviation returned is "<name>"')
def name_value(call_response, name):
    returned_name = call_response.json()["name"]
    actual_name = name
    assert returned_name == actual_name


@then('the capital name returned is "<capital>"')
def capital_value(call_response, capital):
    returned_capital = call_response.json()["capital"]
    actual_capital = capital
    assert returned_capital == actual_capital


@then('the statehood status returned is "<statehood>"')
def statehood_value(call_response, statehood):
    returned_statehood = call_response.json()["statehood"]
    actual_statehood = statehood
    assert returned_statehood == actual_statehood


@then('the list of timezones returned is "<timezones>"')
def timezones_vaue(call_response, timezones):
    returned_timezones = call_response.json()["timezones"]
    actual_timezones = timezones
    assert returned_timezones == actual_timezones


@then('the response status code is 200')
def query_response_code(call_response):
    assert call_response.status_code == 200