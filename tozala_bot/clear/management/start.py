from .commands.runbot import *
from ..models import *

start_letter = "Нажмите кнопку начать, чтобы использовать бота"
start_button = ReplyKeyboardMarkup([[KeyboardButton('🔛Начать')]], resize_keyboard=True, one_time_keyboard=True)
always = ReplyKeyboardMarkup([[KeyboardButton('🔙Назад'), KeyboardButton('🏠Главный страница')]],
                             resize_keyboard=True,
                             one_time_keyboard=True)
credit = ReplyKeyboardMarkup([[KeyboardButton('3 месяца'), KeyboardButton('6 месяца')],
                              [KeyboardButton('12 месяца'), KeyboardButton('🔙Назад')],
                              [KeyboardButton('🏠Главный страница')]], resize_keyboard=True,
                             one_time_keyboard=True)


def operator_list():
    lists = []
    managers = Operator.objects.all()
    for i in managers:
        lists.append(int(i.telegram_id))
    return lists


def start(update, context):
    user_id = update.message.from_user.id
    user = update.message.from_user.username



    if user_id in operator_list():
        update.message.reply_text(start_letter,
                                  reply_markup=start_button)
        try:
            operator = FirstData.objects.filter(operator_tg_id=user_id)
            FirstData.objects.filter(operator_tg_id=user_id).update(step=0)
        except:
            operator = False
        if not operator:
            tel = Operator.objects.get(telegram_id=user_id)
            s = FirstData(operator_name=tel.full_name, operator_tg_id=user_id, operator_phone=tel.phone,
                          operator_user=f"@{user}")
            s.save()
            FirstData.objects.filter(operator_tg_id=user_id).update(step=0)
    else:
        update.message.reply_text(f"ID: {user_id}")


