#FIXED Реализовать рускоязычнуюобертку для всего класса
from util import UfosAutotestUtil

class OperationScroll():

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opKeyScroller(self, driver, keyName):
        # Операция "Кнопка на скроллере"
        # Возможные параметры
        # Название

        # Выставить параметры
        xpathSt = "//button[@title='" + keyName + "']"
        self.util.waitElement(driver, xpathSt)
        driver.find_element_by_xpath(xpathSt).click()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation