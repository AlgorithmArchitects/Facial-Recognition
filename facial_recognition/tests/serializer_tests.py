import unittest
import os
from .. import constants
from ..core.RecognizerSerializer import RecognizerSerializer

class TestSerializerMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.isdir(constants.USER_DATA_DIRECTORY):
            os.mkdir(constants.USER_DATA_DIRECTORY)

    def test_basic_serialize_deserialize(self):
        RecognizerSerializer.serialize_recognizer(2)
        self.assertEqual(2, RecognizerSerializer.deserialize_recognizer())

    def test_can_overwrite_serialized_data(self):
        RecognizerSerializer.serialize_recognizer(2)
        RecognizerSerializer.serialize_recognizer(2)
