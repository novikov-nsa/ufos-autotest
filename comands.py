from util import UfosAutotestUtil
from operationnavigation import OperationNavigation
from operationscroll import OperationScroll
from operation_visual_form import OperationVisualForm

class Сценарий:

    def __init__(self):
        self.session = UfosAutotestUtil()
        self.op_navigation = OperationNavigation()
        self.op_scroller = OperationScroll()
        self.op_visual_form = OperationVisualForm()

    # Общее
    def ОткрытьСессию(self):
        self.session.SessionOpen()

    def ЗакрытьСессию(self):
        self.session.opSessionClose(self.session.driver)

    def Аутентификация(self, адрес, пользователь, пароль):
        self.op_navigation.opLoginNew(driver=self.session.driver,url=адрес, login=пользователь, passwd=пароль)

    # Навигация
    def ОткрытьМенюНавигации(self, путь):
        self.op_navigation.opMenuNavigator(driver=self.session.driver, menuStr=путь)

    # Списковая форма
    def НажатьКнопкуСФ(self, названиеКнопки):
        self.op_scroller.opKeyScroller(driver=self.session.driver, keyName=названиеКнопки)

    # Визуальная форма
    def ПолучитьЗначениеПоля(self, имяПоля, имяПеременной):
        self.op_visual_form.opGetValueField(driver=self.session.driver, fieldName=имяПоля, variablesParamName=имяПеременной)

