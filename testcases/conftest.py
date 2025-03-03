import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print('opening chrome browser')
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print('opening firefox browser')
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print('opening edge browser')
        driver = webdriver.Edge()
    else:
        print('testing in headless mode')
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    yield driver
    return driver

@pytest.fixture(params=[
    ('ashishkumar123@gmail.com','rahul@123456'),
    ('ashishkumar123@gmails.com','rahul@123456'),
    ('ashishkumar123@gmail.com','rahul@12345'),
    ('ashishkumar12@gmail.com','rahul@12')
])
def getloginsdata(request):
    return request.param

def pytest_metadata(metadata):
    metadata['tester']='Rahul'
    metadata['batch'] = 'CT15'
    metadata.pop("System",None)