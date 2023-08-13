"""Defines unittests for BaseModel class"""

import datetime
import os
import unittest
import uuid
from time import sleep

from models.base_model import BaseModel
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittest for User Instantiation"""

    @classmethod
    def setUp(cls):
        """Set up class method"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Tear down class method"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_user_type(self):
        """Test the type of user"""
        self.assertEqual(User, type(User()))

    def test_user_parent(self):
        """Test the type of user"""
        self.assertIsInstance(User(), BaseModel)

    def test_email_is_str(self):
        """Test the type of user"""
        self.assertEqual(str, type(User().email))

    def test_password_is_str(self):
        """Test the type of user"""
        self.assertEqual(str, type(User().password))

    def test_first_name_is_str(self):
        """Test the type of user"""
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_str(self):
        """Test the type of user"""
        self.assertEqual(str, type(User().last_name))

    def test_id_is_str(self):
        """Test the type of user"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_str(self):
        """Test the type of user"""
        self.assertEqual(datetime.datetime, type(User().created_at))

    def test_updated_at_is_str(self):
        """Test the type of user"""
        self.assertEqual(datetime.datetime, type(User().updated_at))

    def test_email_default_value(self):
        """Test the default value of email"""
        self.assertEqual("", User().email)

    def test_password_default_value(self):
        """Test the default value of password"""
        self.assertEqual("", User().password)

    def test_first_name_default_value(self):
        """Test the default value of first_name"""
        self.assertEqual("", User().first_name)

    def test_last_name_default_value(self):
        """Test the default value of last_name"""
        self.assertEqual("", User().last_name)

    def test_email_changing_value(self):
        """Test the changing value of email"""
        obj = User()
        obj.email = "ys@gmail.com"
        self.assertEqual(obj.email, "ys@gmail.com")

    def test_password_changing_value(self):
        """Test the changing value of password"""
        obj = User()
        obj.password = "1234"
        self.assertEqual(obj.password, "1234")

    def test_first_name_changing_value(self):
        """Test the changing value of first_name"""
        obj = User()
        obj.first_name = "salma"
        self.assertEqual(obj.first_name, "salma")

    def test_last_name_changing_value(self):
        """Test the changing value of last_name"""
        obj = User()
        obj.last_name = "yousef"
        self.assertEqual(obj.last_name, "yousef")

    def test_id_when_changing_it(self):
        """Test the changing value of id"""
        obj = User()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        """Test the changing value of created_at"""
        obj = User()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.created_at = t
        self.assertEqual(obj.created_at, t)

    def test_updated_at_when_changing_it(self):
        """Test the changing value of updated_at"""
        obj = User()
        t = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        obj.updated_at = t
        self.assertEqual(obj.updated_at, t)

    def test_creating_new_str_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.name = "salma"
        self.assertEqual(obj.name, "salma")

    def test_creating_new_int_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        """Test the changing value of updated_at"""
        obj = User()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        """Test the uniqueness of id"""
        obj = User()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj2 = User()
        obj3 = User()
        obj4 = User()
        obj5 = User()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        """Test the uniqueness of id"""
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = User()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        """Test the precision of created_at"""
        obj = User()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        """Test the uniqueness of id"""
        obj1 = User()
        sleep(0.05)
        obj2 = User()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        """Test the uniqueness of id"""
        obj1 = User()
        sleep(0.05)
        obj2 = User()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        """Test the uniqueness of id"""
        obj = User()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        """Test the uniqueness of id"""
        obj = User()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        """Test the uniqueness of id"""
        obj = User(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test the uniqueness of id"""
        obj = User(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        """Test the uniqueness of id"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        """Test the uniqueness of id"""
        with self.assertRaises(TypeError):
            User(created_at=datetime.datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        """Test the uniqueness of id"""
        with self.assertRaises(TypeError):
            User(updated_at=datetime.datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_id_when_instantiating_with_dict(self):
        """Test the uniqueness of id"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = User(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        """Test the uniqueness of id"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = User(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        """Test the uniqueness of id"""
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = User(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        """Test the uniqueness of id"""
        obj = User(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestUserSave(unittest.TestCase):
    """Unittests for save method"""

    @classmethod
    def setUp(cls):
        """Set up testing environment"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        """Tear down testing environment"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_ID(self):
        """Test the uniqueness of id"""
        obj = User()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        """Test the uniqueness of id"""
        obj = User()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        """Test the uniqueness of id"""
        obj = User()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        """Test the uniqueness of id"""
        obj = User()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        """Test the uniqueness of id"""
        obj = User()
        obj.save()
        obj_id = "User." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        """Test the return type of to_dict"""
        self.assertEqual(dict, type(User().to_dict()))

    def test_the_returned_keys(self):
        """Test the returned keys of to_dict"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = User()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        """Test the returned dict contains new attribute"""
        obj = User()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        """Test the uniqueness of id"""
        obj = User()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        """Test the uniqueness of id"""
        obj = User()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        """Test the uniqueness of id"""
        obj = User()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        created_time = '2017-09-28T21:03:54.052298'
        self.assertEqual(created_time, obj.to_dict()["updated_at"])

    def test_to_dict_id_to_create_another_instance(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj1_dict = obj1.to_dict()
        obj2 = User(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj1_dict = obj1.to_dict()
        obj2 = User(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj1_dict = obj1.to_dict()
        obj2 = User(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj1_dict = obj1.to_dict()
        obj2 = User(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        """Test the uniqueness of id"""
        obj1 = User()
        obj1_dict = obj1.to_dict()
        obj2 = User(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        """Test the uniqueness of id"""
        obj = User()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        """Test the uniqueness of id"""
        bm = User()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestUserStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        """Test the uniqueness of id"""
        obj = User()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.email = "ys@gmail"
        obj.first_name = "salma"
        obj.last_name = "yousef"
        obj.password = "78526"
        result = "[User] (1234) {'id': '1234', " \
                 "'created_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime.datetime" \
                 "(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'email': 'ys@gmail', 'first_name': "\
                 "'salma', 'last_name': 'yousef', 'password': '78526'}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()
