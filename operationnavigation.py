from util import UfosAutotestUtil

class OperationNavigation():

    def __init__(self):
        self.util = UfosAutotestUtil()

    def opFilterScroller(self, driver,setOperation):
        # TODO Реализовать рускоязычную обертку для метода opFilterScroller
        #Проверить на включенность фильтров
        xpathSt = "//img[@title='Видимость фильтров'][contains(@class,'filterToggler z-image')]"

        self.util.waitElement(driver, xpathSt)
        elem = driver.find_element_by_xpath(xpathSt)
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

    def opLoginNew(self, driver, url, login, passwd):
        driver.get(url)
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys(login)
        driver.find_element_by_id("psw").clear()
        driver.find_element_by_id("psw").send_keys(passwd)
        driver.find_element_by_id("okButton").click()

        resultOperation = {'Статус': 'ОК'}
        return resultOperation


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

            for menuItem in menuStr.split('/'):
                # * Обозначение узла навигации
                if menuItem[0]=='*':
                    xpathSt = "//tr[contains(@class, 'z-treerow')][@title='" + menuItem[1:] + "']"
                    #xpathSt = "//tr[contains(@class, 'z-treecell-text')][@title='" + menuItem[1:] + "']"
                if menuItem[0]!='*':
                    xpathSt = xpathSt+ "/following::tr[contains(@class, 'z-treerow')][@title='" + menuItem + "']"

                self.util.waitElement(driver, xpathSt)
                elemNavigation = driver.find_element_by_xpath(xpathSt)
                elemNavigation.click()

            resaultOperation = {'Статус':'ОК'}
            return resaultOperation