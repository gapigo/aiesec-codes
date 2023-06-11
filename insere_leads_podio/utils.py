def sel(selector, el=None):
    if el:
        el.find_element(By.CSS_SELECTOR, selector)
    return driver.find_element(By.CSS_SELECTOR, selector)

def sels(selector, el=None):
    if el:
        el.find_elements(By.CSS_SELECTOR, selector)
    return driver.find_elements(By.CSS_SELECTOR, selector)

def clicar(el):
    webdriver.ActionChains(driver).move_to_element(el).click(el).perform()