from util import UfosAutotestUtil
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException

class OperationVisualForm:

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opGetValueField(self, driver, fieldName, variablesParamName):

        xpathSt = "//input[@name='" + fieldName + "']"
        self.util.waitElement(driver, xpathSt)

        elem = driver.find_element(By.XPATH, xpathSt)
        fieldValue = elem.get_attribute('value')


        resaultOperation ={'Статус': 'ОК','Переменная':{'Имя параметра':variablesParamName,'Значение':fieldValue}}
        return resaultOperation



    def opSetValueField(self, driver, setOperation):

        # Выставить параметры
        fieldName = setOperation['Поле']
        fieldValue = setOperation['Значение']

        xpathSt = "//input[@name='" + fieldName + "']"
        wait_result = self.util.waitElement(driver, xpathSt)
        if wait_result == 'ok':
            driver.find_element(By.XPATH, xpathSt).clear()
            driver.find_element(By.XPATH, xpathSt).send_keys(fieldValue)
            result = {'Operation': 'Ввести значение в поле', 'dateTimeOperation': datetime.datetime.now(),
                      'result': 'ok'}
        else:
            result = {'Operation': 'Ввести значение в поле', 'dateTimeOperation': datetime.datetime.now(),
                      'result': 'Failed', 'comment': 'Поле для ввода значения не найдено'}

        return result



    def opButtonSave(self, driver, setOperation):

        # Выставить параметры
        if 'Документ' in setOperation:
            if setOperation['Документ'] == 'Дочерний документ': posKey = '2'
            if setOperation['Документ'] == 'Текущий': posKey = '1'
        else:
            posKey = '1'

        xpathSt = "//button[@title='Сохранить изменения']"


        self.util.waitElement(driver, xpathSt)

        element = driver.find_elements_by_xpath(xpathSt)

        if posKey == '1': driver.find_element(By.XPATH, xpathSt).click()
        if posKey == '2': ActionChains(driver).move_to_element(element[1]).click(element[1]).perform()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation




    def opButtonSaveAndClose(self, driver, setOperation):
        # Операция "Кнопка"
        # Возможные параметры
        # Название

        # Выставить параметры

        if 'Документ' in setOperation:
            if setOperation['Документ'] == 'Дочерний документ': posKey = '2'
            if setOperation['Документ'] == 'Текущий': posKey = '1'
        else:
            posKey = '1'


        xpathSt = "//button[@title='Сохранить изменения и закрыть окно']"


        self.util.waitElement(driver, xpathSt)

        element = driver.find_elements_by_xpath(xpathSt)

        if posKey == '1': element.click()
        if posKey == '2': element[1].click()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation


    def opButton(self, driver, setOperation):
        # Операция "Кнопка"
        # Возможные параметры
        # Название

        # Выставить параметры

        keyName = setOperation['Название']
        if 'Порядок' in setOperation:
            elemPos=setOperation['Порядок']
        else:
            elemPos = '1'
        xpathSt = "//body//descendant::button[text() = '" + keyName + "'][" + elemPos + "]"
        self.util.waitElement(driver, xpathSt)
        # driver.find_element_by_xpath(xpathSt).click()

        element = driver.find_element(By.XPATH, xpathSt)
        ActionChains(driver).move_to_element(element).click(element).perform()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation





    def opCheckRadioBut(self, driver, setOperation):
        # Операция "Установить радио кнопку"
        # Возможные параметры
        # Системное имя

        # Выставить параметры
        elemValue = setOperation['Значение']


        # xpathSt = "//label[text()='" + elemValue + "'][@class='z-radio-content']"
        xpathSt = "//input[@type='radio']/following::label[text()='" + elemValue + "']"

        self.util.waitElement(driver, xpathSt)
        elem = driver.find_element(By.XPATH, xpathSt)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation




    def opCheckTrue(self, driver, setOperation):
        # Операция "Установить чекер"
        # Возможные параметры
        # Системное имя

        # Выставить параметры
        elemName=setOperation['Системное имя']

        xpathSt = "//input[@name='" + elemName + "']/following-sibling::div"

        self.util.waitElement(driver, xpathSt)
        elem = driver.find_element(By.XPATH, xpathSt)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation



    def opGoToTabPanel(self, driver, setOperation):
        # Операция "Перейти на закладку"
        # Возможные параметры
        # Название
        # Значение (может принимать = , =~ )

        # Выставить параметры
        panName=setOperation['Название']

        xpathSt = "//span[text()='" + panName + "']/parent::a/parent::li[@class='z-tab']"
        xpathSt2 = "//span[text()='" + panName + "']"

        self.util.waitElement(driver, xpathSt)
        self.util.waitElement(driver, xpathSt2)
        elem = driver.find_element(By.XPATH, xpathSt2)
        driver.execute_script("return arguments[0].scrollIntoView();", elem)
        ActionChains(driver).move_to_element(elem).perform()
        elem.click()
        #ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation



    def opSetlListBox(self, driver, setOperation):
        # Операция "Выбрать из списка"
        # Возможные параметры
        # Название

        # Выставить параметры
        sysKeyName = setOperation['Системное имя кнопки']
        selValue = setOperation['Выбрать']


        # Нажать кнопку выбора
        xpathSt = sysKeyName
        # waitElementName(xpathSt)
        wait_result = self.util.waitElement(driver, xpathSt, reqType='NAME')
        if wait_result == 'ok':
            driver.find_element(By.NAME, xpathSt).click()
            # Выбрать первый попавшийся элемент
            xpathList = "//span[@class='z-comboitem-text'][contains(text(), '" + selValue + "')]"
            #xpathList = "//li[@class='z-comboitem' and @title='" + selValue + "']"
            wait_result2 = self.util.waitElement(driver, xpathList)
            if wait_result2 == 'ok':
                driver.find_element(By.XPATH, xpathList).click()
                result = {'Operation': 'Заполнить поле значением из выпадающего списка', 'dateTimeOperation': datetime.datetime.now(),
                      'result': 'ok'}
            else:
                result = {'Operation': 'Заполнить поле значением из выпадающего списка',
                          'dateTimeOperation': datetime.datetime.now(),
                          'result': 'Failed', 'comment': f'Значение "{selValue}" не найдено'}
        else:
            result = {'Operation': 'Заполнить поле значением из выпадающего списка', 'dateTimeOperation': datetime.datetime.now(),
                      'result': 'Failed', 'comment': 'Поле с выпадающим списком не отображается'}
        return result

    def opSetDict(self, driver, setOperation):
        # Операция "Выбрать из справочника"
        # Возможные параметры
        # Название кнопки
        # Значение (может принимать = , =~ )

        # Выставить параметры
        if 'Название кнопки' in setOperation:
            sysKeyName = setOperation['Название кнопки']
            xpathSt = "//button[text()='" + sysKeyName + "']"
        if 'Подсказка на кнопке' in setOperation:
            sysKeyName = setOperation['Подсказка на кнопке']
            xpathSt = "//button[@title='" + sysKeyName + "']"
        if 'Значение' in setOperation:
            dictValue = setOperation['Значение']
            xpathStDict = "//div[@class='z-listcell-content'][text()='" + dictValue + "']"
            if dictValue[0] == '~': xpathStDict = "//div[@class='z-listcell-content'][contains(text(), '" + dictValue[1:] + "')]"


            self.util.waitElement(driver, xpathSt)
            driver.find_element(By.XPATH, xpathSt).click()

            #print(xpathStDict)

            if dictValue != 'Выбрать любое значение':
                self.util.waitElement(driver, xpathStDict)
                elem = driver.find_element(By.XPATH, xpathStDict)
                ActionChains(driver).move_to_element(elem).click(elem).perform()

            if dictValue == 'Выбрать любое значение':
                # Не работает
                self.util.waitElement(driver, xpathStDict)
                elem = driver.find_element(By.XPATH, xpathStDict)
                ActionChains(driver).move_to_element(elem).click(elem).perform()


            self.util.waitElement(driver, "//button[text()='OK']")
            driver.find_element(By.XPATH, "//button[text()='OK']").click()

            resaultOperation = {'Статус':'ОК'}
            return resaultOperation

    def select_from_dict(self, driver, dict_button_name: str, dict_name: str, columns_where_find: dict, text_to_find: str):

        '''
        :param driver:
        :param dict_button_name: имя кнопки выбора значения из справочника на визуальной форме
        :param dict_name: наименование справочника (справочная информация)
        :param column_where_find: наименование колонок и их значения, которые необходимо найти
        :return:
        '''

        wait_result = self.util.waitElement(driver, dict_button_name, reqType='NAME')
        if wait_result == 'ok':
            driver.find_element(By.NAME, dict_button_name).click()

            for column in columns_where_find:
                x_column = "//input[@filter-for='" + column + "']"
                wait_result_select_form = self.util.waitElement(driver, reqText= x_column)
                if wait_result_select_form == 'ok':
                    driver.find_element(By.XPATH, x_column).clear()
                    if len(columns_where_find[column]) > 0:
                        driver.find_element(By.XPATH, x_column).send_keys(columns_where_find[column])
                else:
                    result = {'Operation': f'Выбрать из справочника "{dict_name}"',
                              'dateTimeOperation': datetime.datetime.now(),
                              'result': 'Failed', 'comment': f'Колонка "{columns_where_find[column]}" не найдена'}
            driver.find_element(By.XPATH, x_column).send_keys(Keys.RETURN)
            # Найти строку для выбора
            x_find_value = "//div[@class='z-listcell-content'][contains(text(), '" + text_to_find + "')]"
            wait_result_find_text = self.util.waitElement(driver, reqText= x_find_value)
            if wait_result_find_text == 'ok':
                driver.find_element(By.XPATH, x_find_value).click()
                wait_result_find_ok_button = self.util.waitElement(driver, "//button[text()='OK']")
                if wait_result_find_ok_button == 'ok':
                    driver.find_element(By.XPATH, "//button[text()='OK']").click()
                    result = {'Operation': f'Выбрать из справочника "{dict_name}"',
                      'dateTimeOperation': datetime.datetime.now(),
                      'result': 'ok'}
                else:
                    result = {'Operation': f'Выбрать из справочника "{dict_name}"',
                              'dateTimeOperation': datetime.datetime.now(),
                              'result': 'Failed', 'comment': f'Кнопка "OK" не найдена'}
            else:
                result = {'Operation': f'Выбрать из справочника "{dict_name}"',
                          'dateTimeOperation': datetime.datetime.now(),
                          'result': 'Failed', 'comment': f'Значение "{text_to_find}" в строке не найдено'}
        else:
            result = {'Operation': f'Выбрать из справочника "{dict_name}"',
                      'dateTimeOperation': datetime.datetime.now(),
                      'result': 'Failed', 'comment': f'Кнопка "{dict_button_name}" не найдена'}
        return result