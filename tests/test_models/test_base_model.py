"""Defines unittests for BaseModel class"""

import datetime
import os
import unittest
import uuid
from time import sleep

import models
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittest for BaseMode Instantiation"""

    @classmethod
    def setUp(cls):
        """Set up test methods"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Tear down test methods"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_base_model_type(self):
        """Test base_model type"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """Check if BaseModel in all dict"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """test_id_is_public_str"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """test_created_at_is_public_datetime"""
        self.assertEqual(datetime.datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """test_updated_at_is_public_datetime"""
        self.assertEqual(datetime.datetime, type(BaseModel().updated_at))

    def test_id_when_changing_it(self):
        """test_id_when_changing_it"""
        obj = BaseModel()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        """test_created_at_when_changing_it"""
        obj = BaseModel()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.created_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_updated_at_when_changing_it(self):
        """test_updated_at_when_changing_it"""
        obj = BaseModel()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.updated_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_creating_new_str_attr_from_instance(self):
        """test_creating_new_str_attr_from_instance"""
        obj = BaseModel()
        obj.name = "salma"
        self.assertEqual(obj.name, "salma")

    def test_creating_new_int_attr_from_instance(self):
        """test_creating_new_int_attr_from_instance"""
        obj = BaseModel()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        """test_creating_new_float_attr_from_instance"""
        obj = BaseModel()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        """test_creating_new_bool_attr_from_instance"""
        obj = BaseModel()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        """test_creating_new_list_attr_from_instance"""
        obj = BaseModel()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        """test_creating_new_dict_attr_from_instance"""
        obj = BaseModel()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        """test_id_is_unique"""
        obj = BaseModel()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        """test_id_is_unique_for_different_instances"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj4 = BaseModel()
        obj5 = BaseModel()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        """test_created_at_with_time_now"""
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = BaseModel()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        """test_created_at_precision"""
        obj = BaseModel()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        """test_two_models_different_created_at"""
        obj1 = BaseModel()
        sleep(0.05)
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        """test_two_models_different_updated_at"""
        obj1 = BaseModel()
        sleep(0.05)
        obj2 = BaseModel()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        """test_updated_at_is_greater_than_created_at"""
        obj = BaseModel()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        """test_updated_at_with_update"""
        obj = BaseModel()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        """test_args_unused"""
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """test_instantiation_with_kwargs"""
        obj = BaseModel(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """test_instantiation_with_None_kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        """test_instantiation_with_datetime_type_for_created_at_kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(created_at=datetime.
                      datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        """test_instantiation_with_datetime_type_for_updated_at_kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(updated_at=datetime.
                      datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_id_when_instantiating_with_dict(self):
        """test_id_when_instantiating_with_dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = BaseModel(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        """test_created_at_when_instantiating_with_dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = BaseModel(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        """test_updated_at_when_instantiating_with_dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = BaseModel(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        obj = BaseModel(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestBaseModelSave(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(cls):
        """set up for all tests"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """teardown for all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_ID(self):
        """test_save_with_ID"""
        obj = BaseModel()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        """test_save_with_created_at"""
        obj = BaseModel()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        """test_save_with_updated_at"""
        obj = BaseModel()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        """test_save_with_arg"""
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """test_save_updates_file"""
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        """test_return_type_of_to_dict"""
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_the_returned_keys(self):
        """test_the_returned_keys"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = BaseModel()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        """test_new_attribute_in_the_dict"""
        obj = BaseModel()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        """test_to_dict_when_changing_id"""
        obj = BaseModel()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        """test_to_dict_when_changing_created_at"""
        obj = BaseModel()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        """test_to_dict_when_changing_updated_at"""
        obj = BaseModel()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["updated_at"])

    def test_to_dict_datetime_attributes_are_strs(self):
        """test type of created_at and updated_at inside dict"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_id_to_create_another_instance(self):
        """test_to_dict_id_to_create_another_instance"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        """test_to_dict_created_at_to_create_another_instance"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        """test_to_dict_updated_at_to_create_another_instance"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        """test_to_dict_object_quality_when_creating_another_instance"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        """test_to_dict_dict_quality_when_creating_another_instance"""
        obj1 = BaseModel()
        obj1_dict = obj1.to_dict()
        obj2 = BaseModel(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        """test_contrast_to_dict_dunder_dict"""
        obj = BaseModel()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        """test_to_dict_with_arg"""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestBaseModelStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        """test_str"""
        obj = BaseModel()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        result = "[BaseModel] (1234) {'id': '1234', " \
                 "'created_at': datetime." \
                 "datetime(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime." \
                 "datetime(2017, 9, 28, 21, 3, 54, 52298)}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()
