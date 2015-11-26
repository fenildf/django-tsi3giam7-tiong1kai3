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
                '網域': 'http://意傳.台灣',
            }
        )
        回應 = self.client.get(
            '/網址',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://意傳.台灣/網址')

    def test_post轉址(self):
        self.client.post(
            '/試驗中介',
            {
                '模式': '轉址',
                '網域': 'http://意傳.台灣',
            }
        )
        回應 = self.client.post(
            '/網址',
            {'欄位': '內容'}
        )

        self.assertEqual(回應.status_code, 302)
        self.assertEqual(回應.url, 'http://意傳.台灣/網址')
