from util import UfosAutotestUtil
from operationnavigation import OperationNavigation
from operationscroll import OperationScroll
from operation_visual_form import OperationVisualForm

class Сценарий:
    user_login = ''
    user_password = ''
    результат_работы = {}
    # todo реализовать механизм фиксации результата выполнения шага сценария
    def __init__(self):
        self.session = UfosAutotestUtil()
        self.op_navigation = OperationNavigation()
        self.op_scroller = OperationScroll()
        self.op_visual_form = OperationVisualForm()

    # Общее
    def ОткрытьСессию(self):
        self.user_login, self.user_password = self.session.readParams()
        self.session.SessionOpen()

    def ЗакрытьСессию(self):
        self.session.opSessionClose(self.session.driver)

    def Аутентификация(self, адрес: str, пользователь: str, пароль: str, iddqd : str, тип_формы):
        self.op_navigation.opLoginNew(driver=self.session.driver,url=адрес, login=пользователь, passwd=пароль, iddqd=iddqd, type_loginform=тип_формы)

    # Навигация
    def ОткрытьМенюНавигации(self, путь):
        self.op_navigation.opMenuNavigator(driver=self.session.driver, menuStr=путь)

    # Списковая форма
    def НажатьКнопкуСФ(self, названиеКнопки):
        self.op_scroller.opKeyScroller(driver=self.session.driver, keyName=названиеКнопки)

    # Визуальная форма
    def ПолучитьЗначениеПоля(self, имяПоля, имяПеременной):
        self.op_visual_form.opGetValueField(driver=self.session.driver, fieldName=имяПоля, variablesParamName=имяПеременной)

    def УстановитьЗначениеВыпадающегоСписка(self, имяКнопки, значение):
        setOperation = {'Системное имя кнопки': имяКнопки, 'Выбрать': значение}
        self.op_visual_form.opSetlListBox(driver=self.session.driver, setOperation=setOperation)

