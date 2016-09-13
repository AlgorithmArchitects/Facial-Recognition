import unittest
from core.RecognizerSerializer import RecognizerSerializer

class TestSerializerMethods(unittest.TestCase):
    def test_basic_serialize_deserialize(self):
        RecognizerSerializer.serialize_recognizer(2)
        self.assertEqual(2, RecognizerSerializer.deserialize_recognizer())

    def test_can_overwrite_serialized_data(self):
        RecognizerSerializer.serialize_recognizer(2)
        RecognizerSerializer.serialize_recognizer(2)
