from vkbottle import Keyboard, KeyboardButtonColor, Text


# Начало ->
def menuKeyboard():
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text('Настройки', {"command": "settings"}), KeyboardButtonColor.SECONDARY)
    return keyboard.get_json()


# Настройки -> subMenuKeyboard()
def subMenuKeyboard():
    keyboard = Keyboard(one_time=False)
    keyboard.add(Text('Оповощения',  {"command": "notify"}), KeyboardButtonColor.SECONDARY)
    keyboard.add(Text('Админ', {"command": "admin"}), KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text('Назад', {"command": "sub_back"}), KeyboardButtonColor.NEGATIVE)
    return keyboard.get_json()


# Настройки -> Оповощения -> subNotifyKeyboard()
def subNotifyKeyboard(changedText = 'Посты: Off',changedState = KeyboardButtonColor.NEGATIVE):
    keyboard = Keyboard(one_time=False)
    keyboard.add(Text(f'{changedText}', {"command": "post_notify"}), changedState)
    return keyboard.get_json()

