from import_export import resources
from import_export.fields import Field

from .models import SecondData


class OrderResource(resources.ModelResource):
    id = Field(attribute="id", column_name="НОМЕР ЗАЯВКА")
    operator_name = Field(attribute="operator_name", column_name="Имя оператора")
    datetime = Field(attribute="datetime", column_name="Время создания заявка")
    datetime_apply = Field(attribute="datetime_apply", column_name="Время получения заявка")
    datetime_distance = Field(attribute="datetime_distance", column_name="Время ответить")
    product = Field(attribute="product", column_name="Наименование товара")
    client_phone = Field(attribute="client_phone", column_name="Телефонный номер")
    date_credit = Field(attribute="date_credit", column_name="Срок рассрочка")
    manager_username = Field(attribute="manager_username", column_name="Менежер")
    shop = Field(attribute="shop", column_name="Магазин")
    answer = Field(attribute="answer", column_name="Ответ")
    discription = Field(attribute="discription", column_name="Причина")

    class Meta:
        model = SecondData
        exclude = ('operator_tg_id', 'operator_user', 'operator_phone', 'front_doc', "back_doc",
                   "card_doc", "manager_tg_id", "status")