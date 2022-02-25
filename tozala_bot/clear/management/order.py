from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from .commands.runbot import *
from ..models import *

def order(update, context):
    user_id = update.message.from_user.id
    msg = update.message.text
    photo = update.message.photo
    step = FirstData.objects.get(operator_tg_id=user_id)
    if user_id in operator_list():
        if step.step == 0 and msg == '🔛Начать':
            FirstData.objects.filter(operator_tg_id=str(user_id)).update(step=1)
            update.message.reply_text('📱 Номер телефона клиента',
                                      reply_markup=ReplyKeyboardMarkup([[KeyboardButton('🏠Главный страница')]],
                                                                       resize_keyboard=True, one_time_keyboard=True))

        elif step.step == 1 and not msg == "🏠Главный страница" and not msg == "🔙Назад" and msg:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=2)
            FirstData.objects.filter(operator_tg_id=user_id).update(client_phone=msg)
            update.message.reply_text('🛍 Название продукта',
                                      reply_markup=always)

        elif step.step == 2 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=user_id).update(step=1)
            update.message.reply_text('📱 Номер телефона клиента',
                                      reply_markup=ReplyKeyboardMarkup([[KeyboardButton('🏠Главный страница')]],
                                                                       resize_keyboard=True, one_time_keyboard=True))

        elif step.step == 2 and not msg == "🏠Главный страница" and not msg == "🔙Назад" and msg:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=3)
            FirstData.objects.filter(operator_tg_id=user_id).update(product=msg)
            update.message.reply_text('📆 Срок рассрочки',
                                      reply_markup=credit)

        elif step.step == 3 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=user_id).update(step=2)
            update.message.reply_text('🛍 Название продукта',
                                      reply_markup=always)

        elif step.step == 3 and not msg == "🏠Главный страница" and not msg == "🔙Назад" and msg:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=4)
            FirstData.objects.filter(operator_tg_id=user_id).update(date_credit=msg)
            update.message.reply_text('1️⃣ Отправьте фотографию лицевой стороны паспорта клиента',
                                      reply_markup=always)
        elif step.step == 4 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=user_id).update(step=3)
            update.message.reply_text('📆 Срок рассрочки',
                                      reply_markup=credit)
        elif step.step == 4 and photo:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=5)
            FirstData.objects.filter(operator_tg_id=user_id).update(front_doc=photo[0].file_id)
            update.message.reply_text('2️⃣ Отправьте фото обратной стороны паспорта клиента',
                                      reply_markup=always)

        elif step.step == 4 and msg != '🏠Главный страница' and len(photo) == 0:
            update.message.reply_text('❗️❗️❗️Только Фото 1️⃣ Отправьте фотографию лицевой стороны паспорта клиента',
                                      reply_markup=always)
        elif step.step == 5 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=str(user_id)).update(step=4)
            update.message.reply_text('1️⃣ Отправьте фотографию лицевой стороны паспорта клиента',
                                      reply_markup=always)

        elif step.step == 5 and photo:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=6)
            FirstData.objects.filter(operator_tg_id=user_id).update(back_doc=photo[0].file_id)
            update.message.reply_text('3️⃣ Отправьте фото пластиковой карты клиента',
                                      reply_markup=always)
        elif step.step == 5 and msg != '🏠Главный страница' and len(photo) == 0:
            update.message.reply_text('❗️❗️❗️Только Фото 2️⃣Отправьте фото обратной стороны паспорта клиента',
                                      reply_markup=always)

        elif step.step == 6 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=user_id).update(step=5)
            update.message.reply_text('2️⃣Отправьте фото обратной стороны паспорта клиента',
                                      reply_markup=always)
        elif step.step == 6 and photo:
            FirstData.objects.filter(operator_tg_id=user_id).update(step=7)
            FirstData.objects.filter(operator_tg_id=user_id).update(card_doc=photo[0].file_id)
            step = FirstData.objects.get(operator_tg_id=user_id)
            context.bot.send_media_group(chat_id=user_id, media=[InputMediaPhoto(f'{step.front_doc}'),
                                                                 InputMediaPhoto(f'{step.back_doc}'),
                                                                 InputMediaPhoto(f'{step.card_doc}',
                                                                                 caption=f'Продукт: {step.product}\nСрок: {step.date_credit}\nТелефон: {step.client_phone}\nОператор: {step.operator_name}, {step.operator_phone}\nUsername: {step.operator_user}')])
            update.message.reply_text("Вы подтверждаете вышеизложенное?",
                                      reply_markup=ReplyKeyboardMarkup(
                                          [[KeyboardButton("📤Отправить")], [KeyboardButton("🔙Назад"),
                                                                             KeyboardButton("🏠Главный страница")]],
                                          one_time_keyboard=True, resize_keyboard=True))

        elif step.step == 6 and msg != '🏠Главный страница' and len(photo) == 0:
            update.message.reply_text('❗️❗️❗️Только Фото 3️⃣Отправьте фото пластиковой карты клиента',
                                      reply_markup=always)




        elif step.step == 7 and msg == '🔙Назад':
            FirstData.objects.filter(operator_tg_id=str(user_id)).update(step=6)
            update.message.reply_text('3️⃣ Отправьте фото пластиковой карты клиента',
                                      reply_markup=always)
        elif step.step == 7 and msg == "📤Отправить":
            operator = Operator.objects.get(telegram_id=user_id)
            shop = Shop.objects.get(pk=operator.shop_id)
            obj = SecondData()
            obj.operator_phone = step.operator_phone
            obj.operator_tg_id = step.operator_tg_id
            obj.operator_user = step.operator_user
            obj.operator_name = step.operator_name
            obj.product = step.product
            obj.date_credit = step.date_credit
            obj.client_phone = step.client_phone
            obj.front_doc = step.front_doc
            obj.back_doc = step.back_doc
            obj.card_doc = step.card_doc
            obj.shop = shop.shop
            obj.save()
            FirstData.objects.filter(operator_tg_id=user_id).update(step=0)
            update.message.reply_text(f"№{obj.id} Заявка отправлен менеджеру, ждите ответа", reply_markup=start_button)
            manager = RiskManagerGroup.objects.all()
            for i in manager:
                context.bot.send_media_group(chat_id=i.telegram_id, media=[InputMediaPhoto(f'{obj.front_doc}'),
                                                                           InputMediaPhoto(f'{obj.back_doc}'),
                                                                           InputMediaPhoto(f'{obj.card_doc}',
caption=f'Номер заявка: {obj.id}\nПродукт: {obj.product}\nСрок: {obj.date_credit}\nТелефон: {obj.client_phone}\nОператор: {obj.operator_name}, {obj.operator_phone}\nUsername: {obj.operator_user}')])
                context.bot.send_message(chat_id=i.telegram_id, text=f"№{obj.id} выберите приложение👇",
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("Начать скоринг", callback_data=f"{obj.id}_select")]]))



        elif msg == '🏠Главный страница':
            FirstData.objects.filter(operator_tg_id=user_id).update(step=0)
            update.message.reply_text(start_letter, reply_markup=start_button)

