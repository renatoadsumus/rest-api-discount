from app import app
import unittest

class TestApp(unittest.TestCase):

    def test_app_is_alive_app_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        print(response.data)
        self.assertEqual(response.status_code,200)

    def test_app_get_param(self):
        tester = app.test_client(self)
        #response = tester.get('/', query_string=dict(total=10))
        response = tester.get('/?total=10')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.data,10)


if __name__ == '__main__':
    unittest.main()