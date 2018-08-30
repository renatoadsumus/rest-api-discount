from app import app
import unittest
import json

class TestApp(unittest.TestCase):

    def test_app_purchase_total_is_11_and_discount_is_10(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(post_total_purchase='11'))

        result_expect = [{'total_discount': 10}]
        result_actual = json.loads(response.data.decode('utf-8'))

        self.assertEqual(result_actual, {'discount': result_expect})
        self.assertEqual(response.status_code, 200)

    def test_app_purchase_total_is_30_and_discount_is_20(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(post_total_purchase='30'))

        result_expect = [{'total_discount': 20}]
        result_actual = json.loads(response.data.decode('utf-8'))

        self.assertEqual(result_actual, {'discount': result_expect})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()