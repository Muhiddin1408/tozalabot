from .commands.runbot import *


def reply(update, context):
    user_id = update.message.from_user.id
    reply = update.message.reply_to_message.text
    msg = update.message.text
    reply, a = reply.split(" ", maxsplit=1)
    try:
        obj = SecondData.objects.get(pk=int(reply[1:]))
    except:
        obj = False

    if obj and obj.status == False and obj.manager_tg_id == user_id and len(obj.answer) > 0:
        text = f"Номер заявка: №{obj.id}\nПродукт: {obj.product}\nСрок: {obj.date_credit}\n"
        text += f"Телефон: {obj.client_phone}\nОтвет: {obj.answer}\nКомментарий: {msg}\nМенежер: {obj.manager_username}"
        context.bot.send_media_group(chat_id=obj.operator_tg_id, media=[InputMediaPhoto(f'{obj.front_doc}'),
                                                                        InputMediaPhoto(f'{obj.back_doc}'),
                                                                        InputMediaPhoto(f'{obj.card_doc}',
                                                                                        caption=text)])
        SecondData.objects.filter(pk=obj.id).update(status=True, discription=msg)

