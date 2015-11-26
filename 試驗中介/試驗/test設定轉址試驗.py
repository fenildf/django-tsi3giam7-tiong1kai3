import json

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

    def test_get轉址(self):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        回應 = self.client.get(
            '/bang7tsi2',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://i3thuan5.tw/bang7tsi2')

    def test_post轉址(self):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        回應 = self.client.post(
            '/bang7tsi2',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://i3thuan5.tw/bang7tsi2')


    def test_網域轉punycode(self):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://意傳.台灣',
            }
        )
        回應 = self.client.get(
            '/bang7tsi2',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://xn--v0qr21b.xn--kpry57d/bang7tsi2')

    def test_路徑愛跳脫(self):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://i3thuan5.tw',
            }
        )
        回應 = self.client.get(
            '/網址',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://i3thuan5.tw/%E7%B6%B2%E5%9D%80')
