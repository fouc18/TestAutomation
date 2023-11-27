
from time import sleep


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    sleep(10)
    context.driver.quit()
