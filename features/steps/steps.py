import json
from time import sleep
import requests
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I open the login page')
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://automationintesting.online/#/admin')


@when('I log in with username "{username}" and password "{password}"')
def log_in(context, username, password):
    username_input = context.driver.find_element('id', 'username')
    password_input = context.driver.find_element('id', 'password')
    submit_button = context.driver.find_element('id', 'doLogin')

    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()


@then('I should be logged in successfully')
def verify_success_login(context):
    assert 'Welcome' in context.driver.page_source


@when('I create room with number "{room_number}" and price "{room_price}"')
def create_room(context, room_number, room_price):
    sleep(5)
    room_number_input = context.driver.find_element('id', 'roomName')
    room_number_input.send_keys(room_number)
    sleep(5)
    room_price_input = context.driver.find_element('id', 'roomPrice')
    room_price_input.send_keys(room_price)
    sleep(5)
    submit_room = context.driver.find_element('id', 'createRoom')
    submit_room.click()


@then('I should see "{room102}" and "{room103}" listed in the rooms')
def verify_rooms_listed(context, room102, room103):
    sleep(5)

    if context.driver.find_element('id', 'roomName102'):
        assert True
    if context.driver.find_element('id', 'roomName103'):
        assert True


@given('the API is accessible')
def step_given_api_accessible(context):
    context.driver = webdriver.Chrome()


@when('I check the API status')
def step_when_check_api_status(context):
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    context.api_status = response.status_code


@then('the API status should be 200')
def step_then_api_status_200(context):
    assert context.api_status == 200, f"Expected API status 200, but got {context.api_status}"


@then('the field completed for ID 5 should be false')
def step_then_check_id_field(context):
    driver = webdriver.Chrome()
    driver.get("https://jsonplaceholder.typicode.com/todos/5")

    try:
        element_id5 = driver.find_element(By.ID, '5')
        value_comp = element_id5.get_attribute('completed')
        if value_comp.lower() == 'false':
            return True
        else:
            return False
    except Exception as e:
        print(f'error: {e}')
    finally:
        context.driver.quit()
