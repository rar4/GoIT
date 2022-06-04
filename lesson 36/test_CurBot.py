import unittest
from unittest.mock import patch
import CurBotFuncAPI


class Crutch:
    """it just works"""

    def __init__(self, json):
        self.json = json

    def json(self):
        return self.json()


class TectCur(unittest.TestCase):
    def test_cur(self):
        with patch('CurBotFuncAPI.requests.get') as moced_get:

            moced_get.return_value.json.return_value = [{'r030': 36, 'txt': 'Австралійський долар', 'rate': 21.0913,
                                              'cc': 'AUD', 'exchangedate': '03.06.2022'}]
            course = CurBotFuncAPI.terminal_cur('AUD')
            moced_get.assert_called_with('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'AUD&date={CurBotFuncAPI.nowerday()}&json')
            self.assertEqual(course, '1 AUD 21.0913 is UAH')


if __name__ == '__main__':
    unittest.main()
