SOURCE_PRIVATBANK = 1
SOURCE_MONOBANK = 2
SOURCE_VKURSE = 3
SOURCE_CHOICES = (
    (1, 'PrivatBank'),
    (2, 'MonoBank'),
    (3, 'VKurse'),
)

CURRENCY_TYPE_USD = 1
CURRENCY_TYPE_EUR = 2
CURRENCY_TYPE_CHOICES = (
    (1, 'USD'),
    (2, 'EUR'),
)

RATE_TYPE_SALE = 1
RATE_TYPE_BUY = 2
RATE_TYPE_CHOICES = (
    (1, 'Sale'),
    (2, 'Buy'),
)
