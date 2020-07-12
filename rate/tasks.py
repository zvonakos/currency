import requests
from celery import shared_task

from rate import model_choices as mch
from rate.utils import to_decimal


@shared_task
def parse_privatbank():
    from rate.models import Rate
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    currency_type_mapper = {
        'USD': mch.CURRENCY_TYPE_USD,
        'EUR': mch.CURRENCY_TYPE_EUR,
    }

    for item in response.json():
        if item['ccy'] not in currency_type_mapper:
            continue

        currency_type = currency_type_mapper[item['ccy']]

        # BUY
        amount = to_decimal(item['buy'])

        last = Rate.objects.filter(
            source=mch.SOURCE_PRIVATBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_BUY,
        ).last()

        if last is not None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_PRIVATBANK,
                currency_type=currency_type,
                type=mch.RATE_TYPE_BUY,
            )

        # SALE
        amount = to_decimal(item['sale'])

        last = Rate.objects.filter(
            source=mch.SOURCE_PRIVATBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_SALE,
        ).last()

        if last is not None or last.amount != amount:
            Rate.objects.create(
                amount=amount,
                source=mch.SOURCE_PRIVATBANK,
                currency_type=currency_type,
                type=mch.RATE_TYPE_SALE,
            )


@shared_task
def parse_monobank():
    from rate.models import Rate
    url_mono = "https://api.monobank.ua/bank/currency"
    response = requests.get(url_mono)
    currency_type_mapper = {
        '840': mch.CURRENCY_TYPE_USD,
        '978': mch.CURRENCY_TYPE_EUR,
    }

    for item_mono in response.json():
        if item_mono['currencyCodeA'] not in currency_type_mapper:
            continue

    currency_type = currency_type_mapper[item_mono['currencyCodeA']]

    # BUY
    amount = to_decimal(item_mono['rateBuy'])

    last = Rate.objects.filter(
        source=mch.SOURCE_MONOBANK,
        currency_type=currency_type,
        type=mch.RATE_TYPE_BUY,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_MONOBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_BUY,
        )

    # SALE
    amount = to_decimal(item_mono['rateSell'])

    last = Rate.objects.filter(
        source=mch.SOURCE_MONOBANK,
        currency_type=currency_type,
        type=mch.RATE_TYPE_SALE,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_MONOBANK,
            currency_type=currency_type,
            type=mch.RATE_TYPE_SALE,
        )


@shared_task
def parse_vkurseusd():
    from rate.models import Rate
    url_vkurseusd = "http://vkurse.dp.ua/course.json"
    response = requests.get(url_vkurseusd)
    currency_type_mapper = {
        'USD': mch.CURRENCY_TYPE_USD
    }

    for item_vkusd in response.json():
        if item_vkusd['Dollar'] not in currency_type_mapper:
            continue

    currency_type = currency_type_mapper[item_vkusd['Dollar']]

    # BUYUSD
    amount = to_decimal(item_vkusd['buy'])

    last = Rate.objects.filter(
        source=mch.SOURCE_VKURSE,
        currency_type=currency_type,
        type=mch.RATE_TYPE_BUY,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            type=mch.RATE_TYPE_BUY,
        )

    # SALEUSD
    amount = to_decimal(item_vkusd['Sale'])

    last = Rate.objects.filter(
        source=mch.SOURCE_VKURSE,
        currency_type=currency_type,
        type=mch.RATE_TYPE_SALE,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            type=mch.RATE_TYPE_SALE,
        )


@shared_task
def parse_vkurseeur():
    from rate.models import Rate
    url_vkurseeur = "http://vkurse.dp.ua/course.json"
    response = requests.get(url_vkurseeur)
    currency_type_mapper = {
        'Euro': mch.CURRENCY_TYPE_EUR
    }

    for item_vkeur in response.json():
        if item_vkeur['Euro'] not in currency_type_mapper:
            continue

    currency_type = currency_type_mapper[item_vkeur['Euro']]

    # BUYEUR
    amount = to_decimal(item_vkeur['Euro'])

    last = Rate.objects.filter(
        source=mch.SOURCE_VKURSE,
        currency_type=currency_type,
        type=mch.RATE_TYPE_BUY,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            type=mch.RATE_TYPE_BUY,
        )

    # SALEEUR
    amount = to_decimal(item_vkeur['Sale'])

    last = Rate.objects.filter(
        source=mch.SOURCE_VKURSE,
        currency_type=currency_type,
        type=mch.RATE_TYPE_SALE,
    ).last()

    if last is not None or last.amount != amount:
        Rate.objects.create(
            amount=amount,
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            type=mch.RATE_TYPE_SALE,
        )


@shared_task
def parse_():
    parse_monobank.delay()
    parse_privatbank.delay()
