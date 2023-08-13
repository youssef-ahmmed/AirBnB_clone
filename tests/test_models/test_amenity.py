"""Defines unittests for BaseModel class"""

import datetime
import os
import unittest
import uuid
from time import sleep

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittest for Amenity Instantiation"""

    @classmethod
    def setUp(cls):
        """Set up testing methods"""
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

    def test_amenity_type(self):
        """Test Amenity type"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_amenity_parent(self):
        """Test Amenity inheritance"""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_name_is_str(self):
        """Test name is str"""
        self.assertEqual(str, type(Amenity().name))

    def test_id_is_str(self):
        """Test id is of type string"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_str(self):
        """Test created_at is of type string"""
        self.assertEqual(datetime.datetime, type(Amenity().created_at))

    def test_updated_at_is_str(self):
        """Test updated_at is of type string"""
        self.assertEqual(datetime.datetime, type(Amenity().updated_at))

    def test_name_default_value(self):
        """Test name is str"""
        self.assertEqual("", Amenity().name)

    def test_name_changing_value(self):
        """Test that change the name value"""
        obj = Amenity()
        obj.name = "salma"
        self.assertEqual(obj.name, "salma")

    def test_id_when_changing_it(self):
        """Test that change the id value"""
        obj = Amenity()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        """Test that change the created_at value"""
        obj = Amenity()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.created_at = t
        self.assertEqual(obj.created_at, t)

    def test_updated_at_when_changing_it(self):
        """Test that change the updated_at value"""
        obj = Amenity()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.updated_at = t
        self.assertEqual(obj.updated_at, t)

    def test_creating_new_int_attr_from_instance(self):
        """Test that create new int attribute"""
        obj = Amenity()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        """Test that create new float attribute"""
        obj = Amenity()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        """Test that create new bool attribute"""
        obj = Amenity()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        """Test that create new list attribute"""
        obj = Amenity()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        """Test that create new dict attribute"""
        obj = Amenity()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        """Test that id is unique"""
        obj = Amenity()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        """Test that id is unique for different instances"""
        obj1 = Amenity()
        obj2 = Amenity()
        obj3 = Amenity()
        obj4 = Amenity()
        obj5 = Amenity()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        """Test that created_at is with the time of creation"""
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = Amenity()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        """Test that created_at is with the precision of one second"""
        obj = Amenity()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        """Test that two models have different created_at"""
        obj1 = Amenity()
        sleep(0.05)
        obj2 = Amenity()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        """Test that two models have different updated_at"""
        obj1 = Amenity()
        sleep(0.05)
        obj2 = Amenity()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        """Test that updated_at is greater than created_at"""
        obj = Amenity()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        """Test that updated_at is with the time of update"""
        obj = Amenity()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        """Test that args are not used"""
        obj = Amenity(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test that create an instance with kwargs"""
        obj = Amenity(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """Test that create an instance with kwargs None"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        """Test that create an instance with datetime type for created_at"""
        with self.assertRaises(TypeError):
            t = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
            Amenity(created_at=t)

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        """Test that create an instance with datetime type for updated_at"""
        with self.assertRaises(TypeError):
            t = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
            Amenity(updated_at=t)

    def test_id_when_instantiating_with_dict(self):
        """Test that create new id attribute"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Amenity(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        """Test that create new created_at attribute"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Amenity(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        """Test that create new updated_at attribute"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Amenity(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        """Test that create an instance with args and kwargs"""
        obj = Amenity(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestAmenitySave(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(cls):
        """Set up for all tests"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Tear down for all tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_ID(self):
        """Test that save method adds id to object"""
        obj = Amenity()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        """Test that save method adds created_at to object"""
        obj = Amenity()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        """Test that save method adds updated_at to object"""
        obj = Amenity()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        """Test that save method doesn't accept args"""
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """Test that save method updates file"""
        obj = Amenity()
        obj.save()
        obj_id = "Amenity." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        """Test that to_dict method returns a dictionary"""
        self.assertEqual(dict, type(Amenity().to_dict()))

    def test_the_returned_keys(self):
        """Test that to_dict method contains correct keys"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = Amenity()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        """Test that it adds a new attribute to the dictionary"""
        obj = Amenity()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        """Test that change the value of attribute"""
        obj = Amenity()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        """Test that change the value of attribute"""
        obj = Amenity()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        """Test that change the value of attribute"""
        obj = Amenity()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["updated_at"])

    def test_to_dict_id_to_create_another_instance(self):
        """Test that create new instance with the same id"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()
        obj2 = Amenity(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        """Test that create new instance with the same created_at"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()
        obj2 = Amenity(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        """Test that create new instance with the same updated_at"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()
        obj2 = Amenity(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        """Test that create new instance with the same __dict__"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()
        obj2 = Amenity(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        """Test that create new instance with the same __dict__"""
        obj1 = Amenity()
        obj1_dict = obj1.to_dict()
        obj2 = Amenity(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        """Test that to_dict method is different from __dict__"""
        obj = Amenity()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        """Test that to_dict method doesn't accept args"""
        bm = Amenity()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestAmenityStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        """Test that __str__ method print correct output"""
        obj = Amenity()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.name = "salma"
        result = "[Amenity] (1234) {'id': '1234', " \
                 "'created_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), 'name': 'salma'}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()
