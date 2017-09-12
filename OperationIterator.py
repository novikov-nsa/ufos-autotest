from selenium.webdriver.common.action_chains import ActionChains
import Util


def opKeyButton(driver,setOperation):
    # Выставить параметры

    if 'Фильтр' in setOperation:      filterValue = setOperation['Фильтр']
    if 'Поле фильтр' in setOperation: nameKeyFilter = setOperation['Поле фильтр']
    if 'Кнопка' in setOperation: key = setOperation['Кнопка']
    if 'Итератор' in setOperation: nameIterator = setOperation['Итератор']

    if filterValue != 'Все строки':
        xpathSt = ".//input[@value='"+filterValue+"']" \
                  "[@name='"+nameKeyFilter+"']/ancestor::div[@class='z-listcell-content']" \
                  "//button[@title='"+key+"']"
        Util.waitElement(driver, xpathSt)
        element = driver.find_element_by_xpath(xpathSt)
        driver.execute_script("return arguments[0].scrollIntoView();", element)
        element.click()
    else:

        xpathSt = "//td[contains(@class,'"+nameIterator+"')]//button[contains(text(),'"+key+"')]"
        print(xpathSt)

        for element in driver.find_elements_by_xpath(xpathSt):
            Util.waitElement(driver, xpathSt)

            elemen = driver.find_element_by_xpath(xpathSt)
            driver.execute_script("return arguments[0].scrollIntoView();", elemen)
            elemen.click()


    resaultOperation = {'Статус':'ОК'}
    return resaultOperation


def opSetDict(driver,setOperation):
    # Выставить параметры
    filterValue = setOperation['Фильтр']
    nameKeyFilter = setOperation['Поле фильтр']
    key = setOperation['Кнопка']
    dictValue = setOperation['Значение']

    xpathSt = ".//input[@value='"+filterValue+"'][@name='"+nameKeyFilter+"']/ancestor::div[@class='z-listcell-content']"
    Util.waitElement(driver, xpathSt)

    xpathSt = xpathSt + "//button[@title='"+key+"']"
    element = driver.find_element_by_xpath(xpathSt)
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    element.click()

    if dictValue != "Любое значение":  xpathStDict = "//div[@class='z-listcell-content'][contains(text(), '" + dictValue + "')]"
    if dictValue == "Любое значение":  xpathStDict = "//div[@class='doc-dialog-content z-center']//tr[@class ='z-listitem']"

    Util.waitElement(driver, xpathSt)
    element = driver.find_element_by_xpath(xpathStDict)

    ActionChains(driver).move_to_element(element).click(element).perform()

    Util.waitElement(driver, "//button[text()='OK']")
    driver.find_element_by_xpath("//button[text()='OK']").click()

    resaultOperation = {'Статус':'ОК'}
    return resaultOperation