import pytest
from selenium import webdriver


# @pytest.fixture(params=['Chrome', 'Firefox'])
@pytest.fixture
def driver(request):

    browser = request.config.getoption('--browser').capitalize()
    # browser = request.param
    print(f'Creating {browser} driver')

    # my_driver = None
    match browser:
        case 'Chrome':
            my_driver = webdriver.Chrome()
        case 'Firefox':
            my_driver = webdriver.Firefox()
        case _:
            raise TypeError(f'Unknown browser {browser}. Available browsers for testing: Chrome, Firefox, Safari')

    # my_driver.implicitly_wait(15)
    # request.cls.driver = my_driver

    yield my_driver
    # yield

    print(f'Closing {browser} driver')
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='Chrome', help='Web browser for test execution [Chrome | Firefox | Safari]'
    )
