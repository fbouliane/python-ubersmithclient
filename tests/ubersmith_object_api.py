import unittest

from mock import Mock

from ubersmith_client import ubersmith_object_api


class UbersmithApiTest(unittest.TestCase):
    def test_client_list(self):
        backend = Mock()
        data = {
            "1001": {
                "city": "Troy",
                }}

        backend.client.list.return_value = data

        object_api = ubersmith_object_api.init(backend=backend)
        returned_object = object_api.client.list()

        self.assertEqual("Troy", returned_object[0].city)
