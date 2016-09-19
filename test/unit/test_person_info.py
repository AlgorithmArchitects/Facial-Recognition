import unittest
import os
import tempfile
import facial_recognition.core.person_info

class TestSerializerMethods(unittest.TestCase):
    def test_basic_read_from_file_search_by_id(self):
        fp = tempfile.NamedTemporaryFile("w", delete=False)
        path = fp.name
        print(path)
        fp.write("idNumber,someName,descriptiveInfo")
        fp.close()
        info = facial_recognition.core.person_info.PersonInfo(path)
        result = info.get("idNumber")

        self.assertEqual(3, result.__len__())
        self.assertEqual("idNumber", result.get("id"))
        self.assertEqual("someName", result.get("name"))
        self.assertEqual("descriptiveInfo", result.get("info"))

    def test_basic_read_from_file_search_by_name(self):
        fp = tempfile.NamedTemporaryFile("w", delete=False)
        path = fp.name
        print(path)
        fp.write("idNumber,someName,descriptiveInfo")
        fp.close()
        info = facial_recognition.core.person_info.PersonInfo(path)
        result = info.get(name="someName")

        self.assertEqual(3, result.__len__())
        self.assertEqual("idNumber", result.get("id"))
        self.assertEqual("someName", result.get("name"))
        self.assertEqual("descriptiveInfo", result.get("info"))

    def test_id_not_present_throws_exception(self):
        found_exception = 0
        fp = tempfile.NamedTemporaryFile("w", delete=False)
        path = fp.name
        print(path)
        fp.write("idNumber,someName,descriptiveInfo")
        fp.close()
        info = facial_recognition.core.person_info.PersonInfo(path)
        try:
            result = info.get("someOtherIdNumber")
        except facial_recognition.core.person_info.PersonNotFoundException:
            found_exception = 1
        self.assertEqual(1, found_exception, "No exception thrown")

    def test_new_data_added_to_dictionary_and_file_still_has_old_info(self):
        fp = tempfile.NamedTemporaryFile("w", delete=False)
        path = fp.name
        print(path)
        fp.write("idNumber,someName,descriptiveInfo")
        fp.close()
        info = facial_recognition.core.person_info.PersonInfo(path)
        info.add("newName", "newInfo")
        result = info.get("idNumber")

        self.assertEqual(3, result.__len__())
        self.assertEqual("idNumber", result.get("id"))
        self.assertEqual("someName", result.get("name"))
        self.assertEqual("descriptiveInfo", result.get("info"))