"""Defines unittests for Place class"""

import datetime
import os
import unittest
import uuid
from time import sleep

from models.base_model import BaseModel
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittest for Place Instantiation"""

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

    def test_place_type(self):
        self.assertEqual(Place, type(Place()))

    def test_place_parent(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_city_id_is_str(self):
        self.assertEqual(str, type(Place().city_id))

    def test_user_id_is_str(self):
        self.assertEqual(str, type(Place().user_id))

    def test_name_is_str(self):
        self.assertEqual(str, type(Place().name))

    def test_description_is_str(self):
        self.assertEqual(str, type(Place().description))

    def test_number_rooms_is_int(self):
        self.assertEqual(int, type(Place().number_rooms))

    def test_number_bathrooms_is_int(self):
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_max_guest_is_int(self):
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night_is_int(self):
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude_is_float(self):
        self.assertEqual(float, type(Place().latitude))

    def test_longitude_is_float(self):
        self.assertEqual(float, type(Place().longitude))

    def test_amenity_ids_is_list(self):
        self.assertEqual(list, type(Place().amenity_ids))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime.datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime.datetime, type(Place().updated_at))

    def test_city_id_default_value(self):
        self.assertEqual(Place().city_id, "")

    def test_user_id_default_value(self):
        self.assertEqual(Place().user_id, "")

    def test_name_default_value(self):
        self.assertEqual(Place().name, "")

    def test_description_default_value(self):
        self.assertEqual(Place().description, "")

    def test_number_rooms_default_value(self):
        self.assertEqual(Place().number_rooms, 0)

    def test_number_bathrooms_default_value(self):
        self.assertEqual(Place().number_bathrooms, 0)

    def test_max_guest_default_value(self):
        self.assertEqual(Place().max_guest, 0)

    def test_price_by_night_default_value(self):
        self.assertEqual(Place().price_by_night, 0)

    def test_latitude_default_value(self):
        self.assertEqual(Place().latitude, 0.0)

    def test_longitude_default_value(self):
        self.assertEqual(Place().longitude, 0.0)

    def test_amenity_ids_default_value(self):
        self.assertEqual(Place().amenity_ids, [])

    def test_city_id_changing_value(self):
        obj = Place()
        obj.city_id = "1234"
        self.assertEqual(obj.city_id, "1234")

    def test_user_id_changing_value(self):
        obj = Place()
        obj.user_id = "1234"
        self.assertEqual(obj.user_id, "1234")

    def test_name_changing_value(self):
        obj = Place()
        obj.name = "yousef"
        self.assertEqual(obj.name, "yousef")

    def test_description_changing_value(self):
        obj = Place()
        obj.description = "beautiful home"
        self.assertEqual(obj.description, "beautiful home")

    def test_number_rooms_changing_value(self):
        obj = Place()
        obj.number_rooms = 4
        self.assertEqual(obj.number_rooms, 4)

    def test_number_bathrooms_changing_value(self):
        obj = Place()
        obj.number_bathrooms = 2
        self.assertEqual(obj.number_bathrooms, 2)

    def test_max_guest_changing_value(self):
        obj = Place()
        obj.max_guest = 2
        self.assertEqual(obj.max_guest, 2)

    def test_price_by_night_changing_value(self):
        obj = Place()
        obj.price_by_night = 2
        self.assertEqual(obj.price_by_night, 2)

    def test_latitude_changing_value(self):
        obj = Place()
        obj.latitude = 2.2
        self.assertEqual(obj.latitude, 2.2)

    def test_longitude_changing_value(self):
        obj = Place()
        obj.longitude = 2.2
        self.assertEqual(obj.longitude, 2.2)

    def test_amenity_ids_changing_value(self):
        obj = Place()
        obj.amenity_ids = ["123", "456"]
        self.assertEqual(obj.amenity_ids, ["123", "456"])

    def test_id_when_changing_it(self):
        obj = Place()
        obj.id = "1234"
        self.assertEqual(obj.id, "1234")

    def test_created_at_when_changing_it(self):
        obj = Place()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.created_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_updated_at_when_changing_it(self):
        obj = Place()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        self.assertEqual(obj.updated_at,
                         datetime.datetime(2017, 9, 28, 21, 5, 54, 119427))

    def test_creating_new_int_attr_from_instance(self):
        obj = Place()
        obj.age = 10
        self.assertEqual(obj.age, 10)

    def test_creating_new_float_attr_from_instance(self):
        obj = Place()
        obj.age = 45.5
        self.assertEqual(obj.age, 45.5)

    def test_creating_new_bool_attr_from_instance(self):
        obj = Place()
        obj.available = False
        self.assertEqual(obj.available, False)

    def test_creating_new_list_attr_from_instance(self):
        obj = Place()
        obj.names = ["salma", "yousef"]
        self.assertEqual(obj.names, ["salma", "yousef"])

    def test_creating_new_dict_attr_from_instance(self):
        obj = Place()
        obj.dct = {"salma": 1, "yousef": 2}
        self.assertEqual(obj.dct, {"salma": 1, "yousef": 2})

    def test_id_is_unique(self):
        obj = Place()
        self.assertNotEqual(obj.id, uuid.uuid4())

    def test_id_is_unique_for_different_instances(self):
        obj1 = Place()
        obj2 = Place()
        obj3 = Place()
        obj4 = Place()
        obj5 = Place()
        id_set = {obj1.id, obj2.id, obj3.id, obj4.id, obj5.id}
        self.assertEqual(len(id_set), 5)

    def test_created_at_with_time_now(self):
        time_now = datetime.datetime.now()
        sleep(0.5)
        obj = Place()
        self.assertGreater(obj.created_at, time_now)

    def test_created_at_precision(self):
        obj = Place()
        now = datetime.datetime.now()
        difference = now - obj.created_at
        max_acceptable_difference = datetime.timedelta(seconds=1)
        self.assertLessEqual(difference, max_acceptable_difference)

    def test_two_models_different_created_at(self):
        obj1 = Place()
        sleep(0.05)
        obj2 = Place()
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_two_models_different_updated_at(self):
        obj1 = Place()
        sleep(0.05)
        obj2 = Place()
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_updated_at_is_greater_than_created_at(self):
        obj = Place()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updated_at_with_update(self):
        obj = Place()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_args_unused(self):
        obj = Place(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_instantiation_with_kwargs(self):
        obj = Place(name="yousef", age=56)
        self.assertIn("yousef", obj.__dict__.values())
        self.assertIn(56, obj.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_datetime_type_for_created_at_kwargs(self):
        with self.assertRaises(TypeError):
            Place(created_at=datetime.datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_instantiation_with_datetime_type_for_updated_at_kwargs(self):
        with self.assertRaises(TypeError):
            Place(updated_at=datetime.datetime(2017, 9, 28, 21, 7, 51, 973308))

    def test_id_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Place(**dict_attr)
        self.assertEqual(obj.id, "123478")

    def test_created_at_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Place(**dict_attr)
        self.assertEqual(obj.created_at, specific_time)

    def test_updated_at_when_instantiating_with_dict(self):
        specific_time = datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)
        dict_attr = {"id": "123478",
                     "created_at": specific_time.isoformat(),
                     "updated_at": specific_time.isoformat()}
        obj = Place(**dict_attr)
        self.assertEqual(obj.updated_at, specific_time)

    def test_instantiation_with_args_and_kwargs(self):
        obj = Place(123, name="salma")
        self.assertIn("salma", obj.__dict__.values())
        self.assertNotIn(123, obj.__dict__.values())


class TestPlaceSave(unittest.TestCase):
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
        obj = Place()
        id_before = obj.id
        obj.save()
        self.assertEqual(obj.id, id_before)

    def test_save_with_created_at(self):
        obj = Place()
        created_before = obj.created_at
        obj.save()
        self.assertEqual(obj.created_at, created_before)

    def test_save_with_updated_at(self):
        obj = Place()
        updated_before = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, updated_before)

    def test_save_with_arg(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = Place()
        obj.save()
        obj_id = "Place." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestPlaceToDict(unittest.TestCase):
    """Unittests for to_dict method"""

    def test_return_type_of_to_dict(self):
        self.assertEqual(dict, type(Place().to_dict()))

    def test_the_returned_keys(self):
        keys = ["id", "created_at", "updated_at", "__class__"]
        obj = Place()
        obj_keys = list(obj.to_dict())
        self.assertEqual(keys.sort(), obj_keys.sort())

    def test_new_attribute_in_the_dict(self):
        obj = Place()
        obj.name = "yousef"
        self.assertIn("yousef", obj.to_dict().values())

    def test_to_dict_when_changing_id(self):
        obj = Place()
        obj.id = "1234"
        self.assertEqual("1234", obj.to_dict()["id"])

    def test_to_dict_when_changing_created_at(self):
        obj = Place()
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["created_at"])

    def test_to_dict_when_changing_updated_at(self):
        obj = Place()
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        self.assertEqual('2017-09-28T21:03:54.052298',
                         obj.to_dict()["updated_at"])

    def test_to_dict_id_to_create_another_instance(self):
        obj1 = Place()
        obj1_dict = obj1.to_dict()
        obj2 = Place(**obj1_dict)
        self.assertEqual(obj1.id, obj2.id)

    def test_to_dict_created_at_to_create_another_instance(self):
        obj1 = Place()
        obj1_dict = obj1.to_dict()
        obj2 = Place(**obj1_dict)
        self.assertEqual(obj1.created_at, obj2.created_at)

    def test_to_dict_updated_at_to_create_another_instance(self):
        obj1 = Place()
        obj1_dict = obj1.to_dict()
        obj2 = Place(**obj1_dict)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_to_dict_object_quality_when_creating_another_instance(self):
        obj1 = Place()
        obj1_dict = obj1.to_dict()
        obj2 = Place(**obj1_dict)
        self.assertNotEqual(obj1, obj2)

    def test_to_dict_dict_quality_when_creating_another_instance(self):
        obj1 = Place()
        obj1_dict = obj1.to_dict()
        obj2 = Place(**obj1_dict)
        self.assertEqual(obj1_dict, obj2.to_dict())

    def test_contrast_to_dict_dunder_dict(self):
        obj = Place()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        bm = Place()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestPlaceStr(unittest.TestCase):
    """Unittests for __str__ method"""

    def test_str(self):
        obj = Place()
        obj.id = "1234"
        obj.created_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.updated_at = datetime.datetime(2017, 9, 28, 21, 3, 54, 52298)
        obj.city_id = "123"
        obj.user_id = "456"
        obj.name = "yousef"
        obj.description = "home is big"
        obj.number_rooms = 5
        obj.number_bathrooms = 2
        obj.max_guest = 3
        obj.price_by_night = 1000
        obj.latitude = 2.2
        obj.longitude = 3.5
        obj.amenity_ids = ["123", "456"]
        result = "[Place] (1234) {'id': '1234', 'created_at': " \
                 "datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'updated_at': datetime." \
                 "datetime(2017, 9, 28, 21, 3, 54, 52298), " \
                 "'city_id': '123', 'user_id': '456', "\
                 "'name': 'yousef', 'description': 'home is big', " \
                 "'number_rooms': 5, 'number_bathrooms': 2, " \
                 "'max_guest': 3, 'price_by_night': 1000, 'latitude': 2.2, " \
                 "'longitude': 3.5, 'amenity_ids': ['123', " \
                 "'456']}"
        self.assertEqual(str(obj), result)


if __name__ == '__main__':
    unittest.main()
