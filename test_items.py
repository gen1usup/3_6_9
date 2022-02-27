import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    busket_button = browser.find_element_by_xpath(
        '//button[@class="btn btn-lg btn-primary btn-add-to-basket" and @type="submit"]')
    assert busket_button is not None
