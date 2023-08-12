"""Defines unittests for BaseModel class"""

import datetime
import os
import unittest
import uuid
from time import sleep

from models.base_model import BaseModel
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittest for Review Instantiation"""

    def test_Review_type(self):
        self.assertEqual(Review, type(Review()))

    def test_Review_parent(self):
        self.assertIsInstance(Review(), BaseModel)

    def test_place_id_is_str(self):
        self.assertEqual(str, type(Review().place_id))

    def test_user_id_is_str(self):
        self.assertEqual(str, type(Review().user_id))

    def test_text_is_str(self):
        self.assertEqual(str, type(Review().text))

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_str(self):
        self.assertEqual(datetime.datetime, type(Review().created_at))

    def test_updated_at_is_str(self):
        self.assertEqual(datetime.datetime, type(Review().updated_at))

    def test_place_id_changing_value(self):
        obj = Review()
        obj.place_id = "5632"
        self.assertEqual(obj.place_id, "5632")

    def test_user_id_changing_value(self):
        obj = Review()
        obj.place_id = "5632"
        self.assertEqual(obj.place_id, "5632")

    def test_text_changing_value(self):
        obj = Review()
        obj.text = "any text"
        self.assertEqual(obj.text, "any text")

    def test_id_when_changing_it(self):
        obj = Review()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        obj = Review()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.created_at = t
        self.assertEqual(obj.created_at, t)

    def test_updated_at_when_changing_it(self):
        obj = Review()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.updated_at = t
        self.assertEqual(obj.updated_at, t)

    def test_creating_new_int_attr_from_instance(self):
        obj = Review()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        obj = Review()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        obj = Review()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        obj = Review()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        obj = Review()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        obj = Review()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        obj1 = Review()
        obj2 = Review()
        obj3 = Review()
        obj4 = Review()
        obj5 = Review()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = Review()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        obj = Review()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        obj1 = Review()
        sleep(0.05)
        obj2 = Review()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        obj1 = Review()
        sleep(0.05)
        obj2 = Review()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        obj = Review()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        obj = Review()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        obj = Review(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        obj = Review(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        with self.assertRaises(TypeError):
            t = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
            Review(created_at=t)

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        with self.assertRaises(TypeError):
            t = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
            Review(updated_at=t)

    def test_id_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Review(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Review(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Review(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        obj = Review(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestReviewSave(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_ID(self):
        obj = Review()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        obj = Review()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        obj = Review()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        obj = Review()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = Review()
        obj.save()
        obj_id = "Review." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestReviewToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        self.assertEqual(dict, type(Review().to_dict()))

    def test_the_returned_keys(self):
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = Review()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        obj = Review()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        obj = Review()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        obj = Review()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        obj = Review()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["updated_at"])

    def test_to_dict_id_to_create_another_instance(self):
        obj1 = Review()
        obj1_dict = obj1.to_dict()
        obj2 = Review(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        obj1 = Review()
        obj1_dict = obj1.to_dict()
        obj2 = Review(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        obj1 = Review()
        obj1_dict = obj1.to_dict()
        obj2 = Review(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        obj1 = Review()
        obj1_dict = obj1.to_dict()
        obj2 = Review(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        obj1 = Review()
        obj1_dict = obj1.to_dict()
        obj2 = Review(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        obj = Review()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        bm = Review()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestReviewStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        obj = Review()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.user_id = "75326"
        obj.place_id = "786323"
        obj.text = "Any text"
        result = "[Review] (1234) {'id': '1234'," \
                 " 'created_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'user_id': '75326', 'place_id': " \
                 "'786323', 'text': 'Any text'}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()