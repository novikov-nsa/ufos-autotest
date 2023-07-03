#FIXED Реализовать рускоязычнуюобертку для всего класса
from util import UfosAutotestUtil
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import datetime



class OperationScroll():

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opKeyScroller(self, driver, keyName):
        # Операция "Кнопка на скроллере"
        # Возможные параметры
        # Название

        # Выставить параметры
        xpathSt = "//button[@title='" + keyName + "']"
        wait_result = self.util.waitElement(driver, xpathSt)
        if wait_result == 'ok':
            try:
                driver.find_element(By.XPATH, xpathSt).click()
            except ElementNotVisibleException:
                resultOperation = {'Operation': 'Нажать кнопку на форме списка', 'dateTimeOperation': datetime.datetime.now(), 'result': 'Failed'}
            else:
                resultOperation = {'Operation': 'Нажать кнопку на форме списка', 'dateTimeOperation': datetime.datetime.now(),
                                   'result': 'Ok'}
        else:
            resultOperation = {'Operation': 'Нажать кнопку на форме списка', 'dateTimeOperation': datetime.datetime.now(),
                               'result': 'Failed'}

        return resultOperation