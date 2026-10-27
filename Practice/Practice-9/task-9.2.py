def convert_currency(amount, rate):
    assert amount >= 0, "Сума не може бути від'ємною"
    assert rate > 0, "Курс валюти повинен бути більшим за нуль"

    if amount == 0:
        return 0.0

    return amount * rate


try:
    source_amount = 100.0
    exchange_rate = 45.0

    result = convert_currency(source_amount, exchange_rate)
    print(f"Сума після конвертації: {result:.2f}")

    convert_currency(-50, 41.5)
except AssertionError as error:
    print(f"Помилка валідації контракту: {error}")
