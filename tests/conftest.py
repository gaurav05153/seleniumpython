import pytest
from selenium import webdriver

from pabeobjects.HomePage import HomePage
from testdata.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass

driver = None
baseclass = BaseClass()
log = baseclass.getLogger()


@pytest.fixture(params=LoginPageData.test_LoginPage_correct_credentials_data)
def get_creds(request):
    return request.param

@pytest.fixture(params=["gaurav05153@gmail.com"])
def get_correct_creds(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

'''@pytest.fixture(scope="function", autouse=True)
def setup(request):
    yield
    homepage = HomePage(driver)
    homepage.get_sign_out_link().click()
    log.info("Clicked on Sign out")'''


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path=r"C:\Frameworks\Python\myseleniumpythonproject\browsers\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path=r"C:\Frameworks\Python\myseleniumpythonproject\browsers\geckodriver-v0.25.0-win64\geckodriver.exe")

    driver.get("http://automationpractice.com")
    print("Automation Practice Website is Opened successfully")
    log.info("Automation Practice Website is Opened successfully")
    driver.delete_all_cookies()
    driver.maximize_window()
    log.info("Browser is Maximized")
    driver.implicitly_wait(10)

    request.cls.driver = driver
    # assigning this local driver to class driver. this driver can be used by all the classes who uses this fixture
    yield
    #homepage = HomePage(driver)
    #homepage.get_sign_out_link().click()
    #log.info("Clicked on Sign out")
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)