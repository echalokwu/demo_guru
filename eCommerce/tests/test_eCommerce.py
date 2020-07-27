"""
Set of test scripts for testing an ecommerce project
Test script is developed using selenium with pytest framework
"""

import sys;

from selenium.webdriver.support.select import Select

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/echalo/Desktop/demo_guru'])
import time
from utils import utils as utils
from selenium.webdriver.common.by import By


def test_verify_item_in_mobile_list_page_sorted_by_name(browser):
    # Go to URL
    browser.get(utils._URL)

    # Verify Title of the page == 'THIS IS DEMO SITE' is shown in home page
    Actual_Title = browser.title
    try:
        assert utils._Expected_Title == Actual_Title
    except AssertionError as e:
        print(Actual_Title, "is the correct title of page")

    # Click on MOBILE menu
    mobile = browser.find_element(By.XPATH, "//a[contains(text(),'Mobile')]")
    mobile.click()

    # Verify Title of the page == 'MOBILE' is shown on mobile list page
    Actual_Title2 = browser.title
    print(Actual_Title2)
    try:
        assert utils._Expected_Title2 == Actual_Title2
    except AssertionError:
        print(utils._Expected_Title2, "is not shown on mobile list page")

    # In the list of all mobile, select "SORT BY" dropdown as name
    element = browser.find_element(By.XPATH, "(//SELECT[@onchange='setLocation(this.value)'])[1]")
    drp = Select(element)
    drp.select_by_visible_text("Name")

    # Verify all products are sorted by name
    x = "name"
    try:
        assert (x in browser.page_source)
        browser.get_screenshot_as_file("/Users/echalo/Desktop/demo_guru/screenshots/Name.png")
        print("all products are sorted by", x)
    except AssertionError:
        print("all products are not sorted by", x)


def test_verify_cost_of_product_in_list_page_and_details_page_are_equal(browser):
    # Go to URL
    browser.get(utils._URL)

    # Click on 'MOBILE' menu
    m = browser.find_element(By.XPATH, "//a[contains(text(),'Mobile')]")
    m.click()

    # In the list of all mobile, read the cost of SONY Xperia mobile. Note this value
    SonyXperiaPrice = browser.find_element(By.XPATH, "//span[contains(text(),'$100.00')]").text
    print(SonyXperiaPrice)

    # Click on Sony Xperia mobile
    browser.find_element(By.ID, "product-collection-image-1").click()

    # Read the Sony Xperia mobile from detail page
    DetailPrice = browser.find_element(By.XPATH, "//span[@class='price']").text
    print(DetailPrice)

    # Compare value in Step 3 & Step 5 == Product Value in list and details page should be equal($100)
    try:
        assert SonyXperiaPrice == DetailPrice
        print("Verified Successfully")
    except AssertionError as e:
        print("Step 3 and 5 not equal")


def test_verify_user_cannot_add_more_product_in_cart_than_product_available_in_store(browser):

    # Go to URL
    browser.get(utils._URL)

    # Click on 'MOBILE' menu
    m = browser.find_element(By.XPATH, "//a[contains(text(),'Mobile')]")
    m.click()

    # In the list of all mobile, click on 'ADD TO CART' for Sony Xperia mobile
    addSonyXperia = browser.find_element(By.XPATH, "(//span[text()='Add to Cart'])[1]")
    addSonyXperia.click()

    # Change 'QTY' value to 1000 and click 'UPDATE' button
    qty = browser.find_element(By.XPATH, "//*[@id='shopping-cart-table']/tbody/tr/td[4]/input")
    qty.clear()
    qty.send_keys(utils._QTY)
    update = browser.find_element(By.XPATH, "//span[text()='Update']")
    update.click()

    # Verify the error message = Error message is displayed: The requested quantity for
    # 'Sony Xperia' is not available
    Actual_Error_Mssg = browser.find_element(By.XPATH, "//p[@class='item-msg error']").text
    print(Actual_Error_Mssg)
    try:
        assert utils._Expected_Error_Mssg == Actual_Error_Mssg
    except AssertionError:
        print(Actual_Error_Mssg, "is the correct error message displayed")

    # Then click on 'EMPTY CART' link in the footer of list of all mobiles
    emptyCart = browser.find_element(By.XPATH, "//span[contains(text(),'Empty Cart')]")
    emptyCart.click()

    # Verify cart is empty = A message "SHOPPING CART IS EMPTY" is shown
    Actual_EmptyCart_Mssg = browser.find_element(By.XPATH, "//h1[contains(text(),'Shopping Cart is Empty')]").text
    try:
        assert utils._Expected_EmptyCart_Mssg == Actual_EmptyCart_Mssg
    except AssertionError:
        print(Actual_EmptyCart_Mssg, "is the correct displayed message")


def test_verify_you_are_able_to_compare_two_product(browser):

    # 1. Go to URL
    browser.get(utils._URL)

    # 2. Click on 'MOBILE' menu
    m = browser.find_element(By.XPATH, "//a[contains(text(),'Mobile')]")
    m.click()

    # 3. In mobile products list, click on 'Add To Compare' for 2 mobiles = Phone 1 - Sony Xperia, Phone 2 - IPHONE
    addSonyXperia = browser.find_element(By.XPATH, "(//a[text()='Add to Compare'])[1]")
    addSonyXperia.click()
    addIphone = browser.find_element(By.XPATH, "(//a[text()='Add to Compare'])[2]")
    addIphone.click()

    mainMobile1 = browser.find_element(By.XPATH, "(//a[text()='Sony Xperia'])[1]").text
    mainMobile2 = browser.find_element(By.XPATH, "(//a[text()='IPhone'])[1]").text

    # 4. Click on 'COMPARE' button
    compare = browser.find_element(By.XPATH, "//button[@class='button']//span//span[contains(text(),'Compare')]")
    compare.click()

    # Switch to new window
    window_before = browser.window_handles[0]
    print(window_before)
    window_after = browser.window_handles[1]
    print(window_after)
    browser.switch_to.window(window_after)

    # 5. Verify the pop-up window and check that the products are reflected
    Actual_Header = browser.find_element(By.XPATH, "//h1[contains(text(),'Compare Products')]").text
    try:
        assert utils._Expected_Header == Actual_Header
    except AssertionError as e:
        print(e)

    # Check products are reflected
    popupMobile1 = browser.find_element(By.XPATH, "//a[contains(text(),'Sony Xperia')]").text
    popupMobile2 = browser.find_element(By.XPATH, "//a[contains(text(),'IPhone')]").text

    try:
        assert mainMobile1 == popupMobile1
    except AssertionError as eg:
        print(eg)

    try:
        assert mainMobile2 == popupMobile2
    except AssertionError as ee:
        print(ee)

    # 6. Close the Popup Windows
    browser.find_element(By.XPATH, "//span[contains(text(),'Close Window')]").click()
    # Switch back to window_before
    browser.switch_to.window(window_before)

