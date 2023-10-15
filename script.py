def focusToElement(driver, by, value, preventScroll):
    JavaScriptFocusToElement = "arguments[0].focus({'preventScroll': arguments[1]})"
    element = driver.find_element(by, value)
    driver.execute_script(JavaScriptFocusToElement, element, preventScroll)
