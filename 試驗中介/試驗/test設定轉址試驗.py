import json
from unittest.mock import patch

from django.test.testcases import TestCase


class 設定轉址試驗(TestCase):

    def test_設定轉址(self):
        回應 = self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://意傳.台灣',
            }
        )

        self.assertEqual(回應.status_code, 200)
        回應資料 = json.loads(回應.content.decode("utf-8"))
        self.assertEqual(回應資料, {
            '結果': '成功',
        })

    @patch('http.client.HTTPConnection')
    def test_有轉址(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        self.client.get(
            '/bang7tsi2',
            {'欄位': '內容'}
        )
        httpMock.assert_called_once_with('i3thuan5.tw')

    @patch('http.client.HTTPConnection')
    def test_get轉址(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        self.client.get('/bang7tsi2')
        httpMock.return_value.request.assert_called_once_with(
            'GET', '/bang7tsi2'
        )

    @patch('http.client.HTTPConnection')
    def test_get轉址敆參數(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        self.client.get(
            '/bang7tsi2',
            {'欄位': '內容'}
        )
        httpMock.return_value.request.assert_called_once_with(
            'GET', '/bang7tsi2?%E6%AC%84%E4%BD%8D=%E5%85%A7%E5%AE%B9'
        )

    @patch('http.client.HTTPConnection')
    def test_post轉址敆參數(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        self.client.post(
            '/bang7tsi2',
            {'欄位': '內容'}
        )
        httpMock.return_value.request.assert_called_once_with(
            'POST', '/bang7tsi2', json.dumps({'欄位': '內容'}).encode()
        )

    @patch('http.client.HTTPConnection')
    def test_網域轉punycode(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://意傳.台灣',
            }
        )
        self.client.get('/bang7tsi2')
        httpMock.assert_called_once_with('xn--v0qr21b.xn--kpry57d')

    @patch('http.client.HTTPConnection')
    def test_路徑愛跳脫(self, httpMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        self.client.get('/網址')
        httpMock.return_value.request.assert_called_once_with(
            'GET', '/%E7%B6%B2%E5%9D%80'
        )

    @patch('http.client.HTTPSConnection')
    def test_https轉址(self, httpsMock):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'https://i3thuan5.tw',
            }
        )
        self.client.get('/bang7tsi2')
        httpsMock.assert_called_once_with('i3thuan5.tw')
