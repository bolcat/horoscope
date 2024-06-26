from django.db import models
class Zodiac(models.Model):
    sign_zodiac = models.CharField(max_length=150)
    description = models.CharField(max_length=1500, default='')

    zodiac_dict = {
        'aries': 'Овен - от 21 марта до 20 апреля, 1-ый знак зодиака.',
        'taurus': 'Телец - от 21 апреля до 21 мая, 2-ой знак зодиака.',
        'gemini': 'Близнецы - от 22 мая до 21 июня, 3-ий знак зодиака.',
        'cancer': 'Рак - от 22 июня до 22 июля, 4-ый знак зодиака.',
        'leo': 'Лев - от 23 июля до 23 августа, 5-ый знак зодиака.',
        'virgo': 'Дева - от 24 августа до 22 сентября, 6-ой знак зодиака.',
        'libra': 'Весы - от 23 сентября до 23 октября, 7-ой знак зодиака.',
        'scorpio': 'Скорпион - от 24 октября до 22 ноября, 8-ой знак зодиака.',
        'sagittarius': 'Стрелец - от 23 ноября до 21 декабря, 9-ый знак зодиака.',
        'capricorn': 'Козерог - от 22 декабря до 20 января, 10-ый знак зодиака.',
        'aquarius': 'Водолей - от 21 января до 18 февраля, 11-ый знак зодиака.',
        'pisces': 'Рыбы - от 19 февраля до 20 марта, 12-ый знак зодиака.'
    }