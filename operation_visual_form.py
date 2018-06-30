from util import UfosAutotestUtil
from selenium.webdriver.common.action_chains import ActionChains

class OperationVisualForm:

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opGetValueField(self, driver, setOperation):

        # Выставить параметры
        fieldName = setOperation['Поле']
        variablesParamName = setOperation['Переменная']


        xpathSt = "//input[@name='" + fieldName + "']"
        self.util.waitElement(driver, xpathSt)

        elem = driver.find_element_by_xpath(xpathSt)
        fieldValue = elem.get_attribute('value')


        resaultOperation ={'Статус': 'ОК','Переменная':{'Имя параметра':variablesParamName,'Значение':fieldValue}}
        return resaultOperation



    def opSetValueField(self, driver, setOperation):

        # Выставить параметры
        fieldName = setOperation['Поле']
        fieldValue = setOperation['Значение']

        xpathSt = "//input[@name='" + fieldName + "']"
        self.util.waitElement(driver, xpathSt)
        driver.find_element_by_xpath(xpathSt).clear()
        driver.find_element_by_xpath(xpathSt).send_keys(fieldValue)

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation



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

        if posKey == '1': driver.find_element_by_xpath(xpathSt).click()
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

        element = driver.find_element_by_xpath(xpathSt)
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
        elem = driver.find_element_by_xpath(xpathSt)
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
        elem = driver.find_element_by_xpath(xpathSt)
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
        elem = driver.find_element_by_xpath(xpathSt2)
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
        self.util.waitElement(driver, xpathSt, reqType='NAME')
        driver.find_element_by_name(xpathSt).click()

        # Выбрать первый попавшийся элемент

        xpathList = "//span[@class='z-comboitem-text'][contains(text(), '" + selValue + "')]"
        self.util.waitElement(driver, xpathList)
        driver.find_element_by_xpath(xpathList).click()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation

    def opSetDict(self, driver,setOperation):
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
            driver.find_element_by_xpath(xpathSt).click()

            #print(xpathStDict)

            if dictValue != 'Выбрать любое значение':
                self.util.waitElement(driver, xpathStDict)
                elem = driver.find_element_by_xpath(xpathStDict)
                ActionChains(driver).move_to_element(elem).click(elem).perform()

            if dictValue == 'Выбрать любое значение':
                # Не работает
                self.util.waitElement(driver, xpathStDict)
                elem = driver.find_element_by_xpath(xpathStDict)
                ActionChains(driver).move_to_element(elem).click(elem).perform()


            self.util.waitElement(driver, "//button[text()='OK']")
            driver.find_element_by_xpath("//button[text()='OK']").click()

            resaultOperation = {'Статус':'ОК'}
            return resaultOperation