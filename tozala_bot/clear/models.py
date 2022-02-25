from django.db import models
from django.utils.datetime_safe import datetime


class Shop(models.Model):
    shop = models.CharField(max_length=30)

    def __str__(self):
        return self.shop

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

class Operator(models.Model):
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    shop = models.ForeignKey(Shop, default=1, on_delete=models.CASCADE,  verbose_name="Магазин")
    telegram_id = models.BigIntegerField()

    def __str__(self):
        return self.full_name


class RiskManagerGroup(models.Model):
    telegram_id = models.BigIntegerField()

    def __str__(self):
        return str(self.telegram_id)


class FirstData(models.Model):
    operator_name = models.CharField(max_length=40, null=True, blank=True)
    operator_tg_id = models.BigIntegerField()
    operator_phone = models.CharField(max_length=30, null=True, blank=True)
    operator_user = models.CharField(max_length=30, null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True)
    front_doc = models.CharField(max_length=300, null=True, blank=True)
    back_doc = models.CharField(max_length=300, null=True, blank=True)
    card_doc = models.CharField(max_length=300, null=True, blank=True)
    date_credit = models.CharField(max_length=10, null=True, blank=True)
    step = models.PositiveIntegerField(default=0)
    client_phone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.operator_name


class SecondData(models.Model):
    operator_name = models.CharField(max_length=40, null=True, blank=True, verbose_name="Имя оператора")
    operator_tg_id = models.BigIntegerField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время создания заявка", null=True)
    datetime_apply = models.DateTimeField(auto_now_add=False, auto_now=False,null=True, blank=True, verbose_name="Время получения заявка")
    datetime_distance = models.CharField(max_length=40, null=True, blank=True, verbose_name="Время ответить")
    operator_user = models.CharField(max_length=30, null=True, blank=True)
    operator_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Номер оператора")
    product = models.CharField(max_length=100, null=True, blank=True, verbose_name="Наименование товара")
    front_doc = models.CharField(max_length=300, null=True, blank=True)
    back_doc = models.CharField(max_length=300, null=True, blank=True)
    card_doc = models.CharField(max_length=300, null=True, blank=True)
    date_credit = models.CharField(max_length=50, null=True, blank=True, verbose_name="Срок рассрочка")
    manager_tg_id = models.BigIntegerField(null=True)
    manager_username = models.CharField(max_length=100, null=True, blank=True, verbose_name="Менежер")
    status = models.BooleanField(default=False)
    shop = models.CharField(max_length=300, null=True, blank=True, verbose_name="Магазин")
    answer = models.CharField(max_length=100, default="", blank=True, verbose_name="Ответ")
    discription = models.TextField(null=True, blank=True, verbose_name="Причина")
    client_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Телефонный номер")

    def __str__(self):
        return self.operator_name

    # @property
    # def datetime_apply(self):
    #     if str(self.manager_username)[0] == "@":
    #         return datetime.now()
    #     else:
    #         pass
    # datetime_apply.fget.short_description = "Время получения заявка"
    #
    # @property
    # def datetime_distance(self):
    #     if str(self.answer)[0] == "✅" or str(self.answer)[0] == "❌":
    #         return datetime.now() - self.datetime_apply
    #     else:
    #         pass
    # datetime_distance.fget.short_description = "Время ответить"



    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

