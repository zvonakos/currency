import requests
from celery import shared_task  # noqa
from rate import model_choices as mch  # noqa
from rate.models import Rate
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
        840: mch.CURRENCY_TYPE_USD,
        978: mch.CURRENCY_TYPE_EUR,
    }

    for item in response.json():

        if item['currencyCodeA'] not in currency_type_mapper:
            continue
        if item['currencyCodeB'] == 980:
            currency_type = currency_type_mapper[item['currencyCodeA']]

    # BUY
    amount = to_decimal(item['rateBuy'])

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
    amount = to_decimal(item['rateSell'])

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
def parse_vkurse():
    url_vk = "http://vkurse.dp.ua/course.json"
    response = requests.get(url_vk)
    currency_type_mapper = {
        'Dollar': mch.CURRENCY_TYPE_USD,
        'Euro': mch.CURRENCY_TYPE_EUR,
    }
    for item in response:
        if item not in currency_type_mapper:
            continue

        currency_type = currency_type_mapper[item]

        # buy
        rate = to_decimal(response[item]['buy'])
        last = Rate.objects.filter(
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            rate_type=mch.RATE_TYPE_BUY,
        ).last()

        if last is None or last.rate != rate:
            Rate.objects.create(
                rate=rate,
                source=mch.SOURCE_VKURSE,
                currency_type=currency_type,
                rate_type=mch.RATE_TYPE_BUY,
            )

        # sale
        rate = to_decimal(response[item]['sale'])
        last = Rate.objects.filter(
            source=mch.SOURCE_VKURSE,
            currency_type=currency_type,
            rate_type=mch.RATE_TYPE_SALE,
        ).last()

        if last is None or last.rate != rate:
            Rate.objects.create(
                rate=rate,
                source=mch.SOURCE_VKURSE,
                currency_type=currency_type,
                rate_type=mch.RATE_TYPE_SALE,
            )


@shared_task
def parse_():
    parse_monobank.delay()
    parse_privatbank.delay()
    parse_vkurse.delay()
