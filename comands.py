from util import UfosAutotestUtil
from operationnavigation import OperationNavigation

class Сценарий:

    def __init__(self):
        self.session = UfosAutotestUtil()
        self.op_navigation = OperationNavigation()

    def ОткрытьСессию(self):
        self.session.SessionOpen()

    def ЗакрытьСессию(self):
        self.session.opSessionClose(self.session.driver)

    def Аутентификация(self, адрес, пользователь, пароль):
        self.op_navigation.opLoginNew(driver=self.session.driver,url=адрес, login=пользователь, passwd=пароль)

    def ОткрытьМенюНавигации(self, путь):
        self.op_navigation.opMenuNavigator(driver=self.session.driver, menuStr=путь)