from check import Check
from loguru import logger
from list_parser import Parser
from config.settings import general
from vkbottle.bot import Bot, Message, MessageEvent
from vkbottle import GroupEventType, GroupTypes, KeyboardButtonColor
from keyboards import menuKeyboard, subMenuKeyboard, subNotifyKeyboard

Check()

#logger.disable('vkbottle')

bot : Bot = Bot(token=general.Token)


def checkAdmin(uid : int):
    with open(general.AdminList, 'r') as adm_list:
        for line in adm_list.readlines():
            if str(uid) in line:
                return 'True'
        adm_list.close()
    return 'False'


@bot.on.message(payload={'command':'start'})
async def start(message : Message):
    parser = Parser()
    parser.newBotUser(message.peer_id)
    await message.answer(f'Добро пожаловать.\n ID: {message.peer_id}.\n AdminPanel: {checkAdmin(message.peer_id)}', keyboard = menuKeyboard())


@bot.on.message(payload={'command':'settings'})
async def settings(message: Message):
    await message.answer(f'Теперь Вы можете настроить оповещения или зайти в админ-панель.\n p.s. если имеете доступ', keyboard = subMenuKeyboard())


@bot.on.message(payload={'command':'notify'})
async def notify(message: Message):
    await message.answer(f'Вы можете влючить или выключить уведомления о новых постах.', keyboard = subNotifyKeyboard())


@bot.on.message(payload={'command':'post_notify'})
async def post_notify(message: Message):
    parser = Parser()
    old_notify_status = parser.updateNotifyList(message.peer_id)
    if old_notify_status == 'true':
        await message.answer(f'Вы успешно изменили настройки уведомлений.', keyboard = subNotifyKeyboard('Посты: Off', KeyboardButtonColor.NEGATIVE))
    elif old_notify_status == 'false':
        await message.answer(f'Вы успешно изменили настройки уведомлений.', keyboard = subNotifyKeyboard('Посты: On', KeyboardButtonColor.POSITIVE))


@bot.on.message()
async def Handler(message : Message):
    pass


bot.run_forever()

