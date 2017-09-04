import Util


def opLogin(driver,setOperation):

    # Выставить параметры
    typePortal = "Без портала"
    iniArg = Util.readStartParam()
    iniServSelenium, iniStend, initUsers = Util.readStartInitParam()

    stendName = iniArg['Stend']
    url = iniStend[stendName]['Url']
    typeUser=setOperation['Пользователь']
    userLogin= initUsers[stendName][typeUser]['login']
    userPassword = initUsers[stendName][typeUser]['password']


        # Открыть в браузере

    driver.get(url)

    if typePortal == 'ДЭПР':
        Util.waitElement(driver,"IDToken1", reqType='ID')

        driver.find_element_by_id("IDToken1").clear()
        driver.find_element_by_id("IDToken1").send_keys(userLogin)
        driver.find_element_by_id("IDToken2").clear()
        driver.find_element_by_id("IDToken2").send_keys(userPassword)
        driver.find_element_by_name("Login.Submit").click()

        xpathList = "//a[contains(@class,'navbar-nav-a')][contains(text(), 'Тарифное регулирование')]"
        Util.waitElement(driver,xpathList)
        driver.find_element_by_xpath(driver,xpathList).click()

    if typePortal == 'Без портала':
        # Ожидание появления поля
        Util.waitElement(driver,"user", reqType='ID')

        # Ввод значения
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys(userLogin)
        driver.find_element_by_id("psw").clear()
        driver.find_element_by_id("psw").send_keys(userPassword)
        driver.find_element_by_id("okButton").click()

    resaultOperation = '[Операция выполнена]'
    return resaultOperation


def opMenuNavigator(driver,setOperation):
        # Операция "Открыть в меню навигации"
        # Возможные параметры
        # Путь (Задается через разделитель / знак * означает корневой элемент)

        # Выставить параметры
        menuStr = setOperation['Путь']


        for menuItem in menuStr.split('/'):
            # * Обозначение узла навигации
            if menuItem[0]=='*':
                xpathSt = "//tr[contains(@class, 'z-treerow')][@title='" + menuItem[1:] + "']"
            if menuItem[0]!='*':
                xpathSt = xpathSt+ "/following::tr[contains(@class, 'z-treerow')][@title='" + menuItem + "']"

            Util.waitElement(driver,xpathSt)
            elemNavigation = driver.find_element_by_xpath(xpathSt)
            elemNavigation.click()

        resaultOperation = '[Операция выполнена -] '
        return resaultOperation