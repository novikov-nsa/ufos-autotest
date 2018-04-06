import Util

def opKeyScroller(driver, setOperation):
    # Операция "Кнопка на скроллере"
    # Возможные параметры
    # Название

    # Выставить параметры
    keyName = setOperation['Название']

    xpathSt = "//button[@title='" + keyName + "']"
    Util.waitElement(driver, xpathSt)
    driver.find_element_by_xpath(xpathSt).click()

    resaultOperation = {'Статус':'ОК'}
    return resaultOperation