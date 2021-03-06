# Generated by Django 4.0.2 on 2022-02-25 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_name', models.CharField(blank=True, max_length=40, null=True)),
                ('operator_tg_id', models.BigIntegerField()),
                ('operator_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('operator_user', models.CharField(blank=True, max_length=30, null=True)),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('front_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('back_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('card_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('date_credit', models.CharField(blank=True, max_length=10, null=True)),
                ('step', models.PositiveIntegerField(default=0)),
                ('client_phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskManagerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Имя оператора')),
                ('operator_tg_id', models.BigIntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания заявка')),
                ('datetime_apply', models.DateTimeField(blank=True, null=True, verbose_name='Время получения заявка')),
                ('datetime_distance', models.CharField(blank=True, max_length=40, null=True, verbose_name='Время ответить')),
                ('operator_user', models.CharField(blank=True, max_length=30, null=True)),
                ('operator_phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер оператора')),
                ('product', models.CharField(blank=True, max_length=100, null=True, verbose_name='Наименование товара')),
                ('front_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('back_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('card_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('date_credit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Срок рассрочка')),
                ('manager_tg_id', models.BigIntegerField(null=True)),
                ('manager_username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Менежер')),
                ('status', models.BooleanField(default=False)),
                ('shop', models.CharField(blank=True, max_length=300, null=True, verbose_name='Магазин')),
                ('answer', models.CharField(blank=True, default='', max_length=100, verbose_name='Ответ')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='Причина')),
                ('client_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('telegram_id', models.BigIntegerField()),
                ('shop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clear.shop', verbose_name='Магазин')),
            ],
        ),
    ]
