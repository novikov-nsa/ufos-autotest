import sys
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

    def Аутентификация(self, адрес: str, пользователь: str, пароль: str, iddqd=None , тип_формы='basic'):
        result = self.op_navigation.opLoginNew(driver=self.session.driver,url=адрес, login=пользователь, passwd=пароль,
                                               iddqd=iddqd, type_loginform=тип_формы)
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" по адресу "{адрес}", пользователь "{пользователь}", '
                  f'за пользователя "{iddqd}" не пройден')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(
                f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" по адресу "{адрес}", пользователь "{пользователь}", '
                f'за пользователя "{iddqd}" пройден')


    # Навигация
    def ОткрытьМенюНавигации(self, путь):
        result = self.op_navigation.opMenuNavigator(driver=self.session.driver, menuStr=путь)
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" по адресу "{путь}" не пройден')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(f'{result["dateTimeOperation"]}, шаг {result["Operation"]} по адресу "{путь}" пройден')

    # Списковая форма
    def НажатьКнопкуСФ(self, названиеКнопки):
        result = self.op_scroller.opKeyScroller(driver=self.session.driver, keyName=названиеКнопки)
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" с именем "{названиеКнопки}" не пройден')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(f'{result["dateTimeOperation"]}, шаг {result["Operation"]} с именем "{названиеКнопки}" пройден')

    # Визуальная форма
    def ПолучитьЗначениеПоля(self, имяПоля, имяПеременной):
        self.op_visual_form.opGetValueField(driver=self.session.driver, fieldName=имяПоля, variablesParamName=имяПеременной)

    def УстановитьЗначениеВыпадающегоСписка(self, имяКнопки, значение):
        setOperation = {'Системное имя кнопки': имяКнопки, 'Выбрать': значение}
        result = self.op_visual_form.opSetlListBox(driver=self.session.driver, setOperation=setOperation)
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" с именем "{имяКнопки}" не пройден')
            if 'comment' in result.keys():
                print(f'{result["comment"]}')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(f'{result["dateTimeOperation"]}, шаг {result["Operation"]} с именем "{имяКнопки}" пройден')

    def УстановитьЗначениеПоля(self, поле, значение):
        result = self.op_visual_form.opSetValueField(driver=self.session.driver, setOperation={'Поле': поле, 'Значение': значение})
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" в поле "{поле}"  значение "{значение}" не пройден')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" в поле "{поле}"  значение "{значение}" пройден')

    def ВыбратьИзСправочника(self, имяКнопки, справочник, фильтр, текст_в_строке):
        result = self.op_visual_form.select_from_dict(driver=self.session.driver, dict_button_name=имяКнопки, dict_name=справочник,
                                                      columns_where_find=фильтр, text_to_find=текст_в_строке)
        if result['result'] == 'Failed':
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" не пройден')
            if 'comment' in result.keys():
                print(f'{result["comment"]}')
            self.session.driver.close()
            sys.exit(10)
        else:
            print(f'{result["dateTimeOperation"]}, шаг "{result["Operation"]}" пройден')
    def НажатьКнопку(self):
        pass

