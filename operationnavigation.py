import datetime
from util import UfosAutotestUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException

class OperationNavigation():

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opFilterScroller(self, driver,setOperation):
        # TODO Реализовать рускоязычную обертку для метода opFilterScroller
        #Проверить на включенность фильтров
        xpathSt = "//img[@title='Видимость фильтров'][contains(@class,'filterToggler z-image')]"

        self.util.waitElement(driver, xpathSt)
        elem = driver.find_element(By.XPATH, xpathSt)
        src = elem.get_attribute('src')

        src = (src.split(';'))[0]
        src = src.split('/')
        src = src[len(src)-1]
        if src == 'filter_on.png':
            elem.clic()

        #//div[contains(@class,'z-listheader-content')]
        #//th[contains(@class,'z-auxhead')]//input
        #Очистить фильтр
        xpathSt = "//th[contains(@class,'z-auxhead')]//input"
        elements = driver.find_elements_by_xpath(xpathSt)
        for filtItem in elements:
            filtItem.clear()

        resaultOperation = {'Статус':'ОК'}
        return resaultOperation

    def opLoginNew(self, driver, url, login, passwd, iddqd, type_loginform):
        '''

        :param driver: объект Selenium
        :param url: URL приложения
        :param login: Имя пользователя
        :param passwd: Пароль
        :param iddqd: логин пользователя от имени которого происходит вход
        :param type_loginform: тип формы (sso - форма аутентификации с через keycloak, basic - основная форма аутентификации)
        :return:
        '''
        driver.get(url)
        if type_loginform == 'basic':
            login_element_id = 'user'
            password_element_id = 'psw'
            button_element_id = 'okButton'
        elif type_loginform == 'sso':
            login_element_id = 'username'
            password_element_id = 'password'
            button_element_id = 'kc-login'
        else:
            return {'Статус': 'ERROR'}
        try:
            WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID,login_element_id))
        except ElementNotVisibleException:
            result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(), 'result': 'Failed'}
        else:
            try:
                driver.find_element(By.ID, login_element_id)
            except ElementNotVisibleException:
                result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(),
                          'result': 'Failed', 'comment': 'Елемент для ввода имени полььзователя не отображается'}
            else:
                driver.find_element(By.ID, login_element_id).clear()
                driver.find_element(By.ID, login_element_id).send_keys(login)
                try:
                    driver.find_element(By.ID, password_element_id)
                except ElementNotVisibleException:
                    result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(),
                              'result': 'Failed', 'comment': 'Элемент для ввода пароля не отображается'}
                else:
                    driver.find_element(By.ID, password_element_id).clear()
                    driver.find_element(By.ID, password_element_id).send_keys(passwd)
                    try:
                        driver.find_element(By.ID, button_element_id)
                    except ElementNotVisibleException:
                        result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(),
                                  'result': 'Failed', 'comment': 'Кнопка для подтверждения входа не отображается'}
                    else:
                        driver.find_element(By.ID, button_element_id).click()
                        result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(),
                                  'result': 'ok'}
                        if iddqd is not None:
                            try:
                                driver.find_element(By.ID, "rpl")
                            except ElementNotVisibleException:
                                result = {'Operation': 'Аутентификация', 'dateTimeOperation': datetime.datetime.now(),
                                          'result': 'Failed',
                                          'comment': 'Поле для ввода реального пользователя не отображается'}
                            else:
                                driver.find_element(By.ID, "rpl").clear()
                                driver.find_element(By.ID, "rpl").send_keys(iddqd)
        return result


    #def opLogin(self, driver,setOperation):

    #   # Выставить параметры
    #    iniArg = self.util.readStartParam()
    #    iniServSelenium, iniStend, initUsers = self.util.readStartInitParam()

    #    stendName = iniArg['Stend']
    #    url = iniStend[stendName]['Url']
    #    typePortal = iniStend[stendName]['portal']
    #    typeUser=setOperation['Пользователь']
    #    userLogin= initUsers[stendName][typeUser]['login']
    #    userPassword = initUsers[stendName][typeUser]['password']


    #    driver.get(url)

    #    if typePortal == 'DEPR':
    #        self.util.waitElement(driver, "IDToken1", reqType='ID')

    #        driver.find_element_by_id("IDToken1").clear()
    #        driver.find_element_by_id("IDToken1").send_keys(userLogin)
    #        driver.find_element_by_id("IDToken2").clear()
    #        driver.find_element_by_id("IDToken2").send_keys(userPassword)
    #        driver.find_element_by_name("Login.Submit").click()

    #        xpathList = "//a[contains(@class,'navbar-nav-a')][contains(text(), 'Тарифное регулирование')][not(@href='unsafe:javascript:void(0)')]"
    #        self.util.waitElement(driver, xpathList)
    #        driver.find_element_by_xpath(xpathList).click()

    #        xpathSt = "//iframe[@z_xsrc]"
    #        self.util.waitElement(driver, xpathSt)
    #        driver.switch_to_frame(driver.find_element_by_xpath(xpathSt))
    #        xpathSt = "//tr[contains(@class, 'z-treerow')]"
    #        self.util.waitElement(driver, xpathSt)

    #    if typePortal == 'false':
            # Ожидание появления поля
    #        self.util.waitElement(driver, "user", reqType='ID')

            # Ввод значения
    #        driver.find_element_by_id("user").clear()
    #        driver.find_element_by_id("user").send_keys(userLogin)
    #        driver.find_element_by_id("psw").clear()
    #        driver.find_element_by_id("psw").send_keys(userPassword)
    #        driver.find_element_by_id("okButton").click()

    #    resaultOperation = {'Статус':'ОК'}
    #    return resaultOperation


    def opMenuNavigator(self, driver, menuStr):
            # Операция "Открыть в меню навигации"
            # Возможные параметры
            # Путь (Задается через разделитель / знак * означает корневой элемент)

            # Выставить параметры
            error = False
            for menuItem in menuStr.split('/'):
                # * Обозначение узла навигации
                if menuItem[0]=='*':
                    xpathSt = "//tr[contains(@class, 'z-treerow')][@title='" + menuItem[1:] + "']"
                    #xpathSt = "//tr[contains(@class, 'z-treecell-text')][@title='" + menuItem[1:] + "']"
                if menuItem[0]!='*':
                    xpathSt = xpathSt+ "/following::tr[contains(@class, 'z-treerow')][@title='" + menuItem + "']"

                wait_result = self.util.waitElement(driver, xpathSt)
                if wait_result == 'ok':
                    elemNavigation = driver.find_element(By.XPATH, xpathSt)
                    elemNavigation.click()
                else:
                    error = True
            if error:
                result_text = 'Failed'
            else:
                result_text = 'Ok'
            resultOperation = {'Operation': 'Выбрать пункт меню навигации',
                                   'dateTimeOperation': datetime.datetime.now(), 'result': result_text}
            return resultOperation