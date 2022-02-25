from .commands.runbot import *
from datetime import datetime, timezone


def inline(update, context):
    user_id = update.callback_query.from_user.id
    username = update.callback_query.from_user.username
    data = update.callback_query.data
    data = data.split("_")
    if len(data) == 2 and data[1] == "select":
        SecondData.objects.filter(pk=data[0]).update(datetime_apply=datetime.now(timezone.utc))
        update.callback_query.message.edit_text(
            f"№{data[0]} @{update.callback_query.from_user.username} отвечает на заявка",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("✅Одобрено", callback_data=f"{data[0]}_{user_id}_yes"),
                  InlineKeyboardButton("❌Отказ", callback_data=f"{data[0]}_{user_id}_no")]]))
        SecondData.objects.filter(pk=data[0]).update(manager_tg_id=user_id, manager_username=f"@{username}")
    elif len(data) == 3 and data[2] == "yes" and int(data[1]) == user_id:
        SecondData.objects.filter(pk=data[0]).update(answer="✅Одобрено")
        obj = SecondData.objects.get(pk=data[0])
        date = datetime.now(timezone.utc) - obj.datetime_apply
        SecondData.objects.filter(pk=data[0]).update(datetime_distance=str(date)[:7])
        update.callback_query.message.edit_text(
            f"№{data[0]} @{update.callback_query.from_user.username}  ответил на заявка №{data[0]}, Ответ: {obj.answer}")


    elif len(data) == 3 and data[2] == "no" and int(data[1]) == user_id:
        SecondData.objects.filter(pk=data[0]).update(answer="❌Отказ")
        obj = SecondData.objects.get(pk=data[0])
        date = datetime.now(timezone.utc) - obj.datetime_apply
        SecondData.objects.filter(pk=data[0]).update(datetime_distance=str(date)[:7])
        update.callback_query.message.edit_text(
            f"№{data[0]} @{update.callback_query.from_user.username} ответил на заявка №{data[0]}, Ответ: {obj.answer}")
