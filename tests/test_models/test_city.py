"""Defines unittests for City class"""


import datetime
import os
import unittest
import uuid
from time import sleep

from models.city import City
from models.base_model import BaseModel


class TestCityInstantiation(unittest.TestCase):
    """Unittest for City Instantiation"""

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

    def test_city_type(self):
        """Test type of city"""
        self.assertEqual(City, type(City()))

    def test_city_parent(self):
        """Test parent of city"""
        self.assertIsInstance(City(), BaseModel)

    def test_state_id_is_str(self):
        """Test state_id is a string"""
        self.assertEqual(str, type(City().state_id))

    def test_name_is_str(self):
        """Test name is a string"""
        self.assertEqual(str, type(City().name))

    def test_id_is_public_str(self):
        """Test id is a public class attribute of type string"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test created_at is a public class attribute of type datetime"""
        self.assertEqual(datetime.datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test updated_at is a public class attribute of type datetime"""
        self.assertEqual(datetime.datetime, type(City().updated_at))

    def test_state_id_default_value(self):
        """Test state_id default value"""
        self.assertEqual(City().state_id, "")

    def test_name_default_value(self):
        """Test name default value"""
        self.assertEqual(City().name, "")

    def test_state_id_changing_value(self):
        """Test state_id changing value"""
        obj = City()
        obj.state_id = "1234"
        self.assertEqual(obj.state_id, "1234")

    def test_name_changing_value(self):
        """Test name changing value"""
        obj = City()
        obj.name = "yousef"
        self.assertEqual(obj.name, "yousef")

    def test_id_when_changing_it(self):
        """Test id when changing it"""
        obj = City()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        """Test created_at when changing it"""
        obj = City()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.created_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_updated_at_when_changing_it(self):
        """Test updated_at when changing it"""
        obj = City()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.updated_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_creating_new_int_attr_from_instance(self):
        """Test creating new int attribute from instance"""
        obj = City()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        """Test creating new float attribute from instance"""
        obj = City()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        """Test creating new bool attribute from instance"""
        obj = City()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        """Test creating new list attribute from instance"""
        obj = City()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        """Test creating new dict attribute from instance"""
        obj = City()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        """Test id is unique"""
        obj = City()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        """Test id is unique for different instances"""
        obj1 = City()
        obj2 = City()
        obj3 = City()
        obj4 = City()
        obj5 = City()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        """Test created_at with time now"""
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = City()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        """Test created_at precision"""
        obj = City()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        """Test two models have different created_at"""
        obj1 = City()
        sleep(0.05)
        obj2 = City()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        """Test two models have different updated_at"""
        obj1 = City()
        sleep(0.05)
        obj2 = City()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        """Test updated_at is greater than created_at"""
        obj = City()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        """Test updated_at with update"""
        obj = City()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        """Test if no args passed to City"""
        obj = City(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs"""
        obj = City(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        """Test instantiation with datetime type for created_at kwargs"""
        with self.assertRaises(TypeError):
            City(created_at=datetime.
                 datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        """Test instantiation with datetime type for updated_at kwargs"""
        with self.assertRaises(TypeError):
            City(updated_at=datetime.
                 datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_id_when_instantiating_with_dict(self):
        """Test id when instantiating with dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = City(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        """Test created_at when instantiating with dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = City(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        """Test updated_at when instantiating with dict"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = City(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        """Test instantiation with args and kwargs"""
        obj = City(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestCitySave(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(cls):
        """Set up for all tests that will be run"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Tear down for all tests that have been run"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_ID(self):
        """Test save method with passing ID"""
        obj = City()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        """Test save method with passing created_at"""
        obj = City()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        """Test save method with passing updated_at"""
        obj = City()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        """Test save method with passing arg"""
        obj = City()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """Test save method to check if it updates the file"""
        obj = City()
        obj.save()
        obj_id = "City." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestCityToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        """Test the return type of to_dict method"""
        self.assertEqual(dict, type(City().to_dict()))

    def test_the_returned_keys(self):
        """Test the returned keys of to_dict method"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = City()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        """Test new attribute in the dict returned by to_dict method"""
        obj = City()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        """Test to_dict method when changing the id of the object"""
        obj = City()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        """Test to_dict method when changing the created_at attribute"""
        obj = City()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        """Test to_dict method when changing the updated_at attribute"""
        obj = City()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["updated_at"])

    def test_to_dict_id_to_create_another_instance(self):
        """Test to_dict method to create another instance"""
        obj1 = City()
        obj1_dict = obj1.to_dict()
        obj2 = City(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        """Test to_dict method to create another instance"""
        obj1 = City()
        obj1_dict = obj1.to_dict()
        obj2 = City(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        """Test to_dict method to create another instance"""
        obj1 = City()
        obj1_dict = obj1.to_dict()
        obj2 = City(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        """Test to_dict method to create another instance"""
        obj1 = City()
        obj1_dict = obj1.to_dict()
        obj2 = City(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        """Test to_dict method to create another instance"""
        obj1 = City()
        obj1_dict = obj1.to_dict()
        obj2 = City(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        """Test to_dict method and it's return with __dict__"""
        obj = City()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with passing arg"""
        bm = City()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestCityStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        """Test __str__ method"""
        obj = City()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.state_id = "123456"
        obj.name = "yousef"
        result = "[City] (1234) {'id': '1234', 'created_at': " \
                 "datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime." \
                 "datetime(2017, 9, 28, 21, 3, 54, 52298)," \
                 " 'state_id': '123456', " \
                 "'name': 'yousef'}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()
