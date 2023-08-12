"""Defines unittests for FileStorage class"""

import os
import unittest


from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for module instantiation"""

    def test_file_storage_type(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_storage_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            FileStorage().__file_path

    def test_objects_attribute_is_private(self):
        with self.assertRaises(AttributeError):
            FileStorage().__objects

    def test_type_of_private_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_type_of_private_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorageAll(unittest.TestCase):
    """Unittests for all method"""

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
        FileStorage._FileStorage__objects = {}

    def test_all_return_type(self):
        self.assertEqual(dict, type(FileStorage().all()))

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_all_without_creating_objects(self):
        self.assertEqual({}, FileStorage().all())

    def test_all_when_creating_different_objects(self):
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = Place()
        obj5 = City()
        obj6 = Amenity()
        obj7 = Review()
        obj_set = {obj1, obj2, obj3, obj4, obj5, obj6, obj7}
        self.assertEqual(set(storage.all().values()), obj_set)


class TestFileStorageNew(unittest.TestCase):
    """Unittests for new method"""

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
        FileStorage._FileStorage__objects = {}

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage().new(BaseModel(), 123)

    def test_new_with_none(self):
        with self.assertRaises(AttributeError):
            FileStorage().new(None)

    def test_new_before_and_after_calling(self):
        obj = FileStorage()
        obj_dict = obj.all().copy()
        obj.new(User())
        self.assertNotEqual(obj_dict, obj.all())

    def test_new_with_object(self):
        obj1 = BaseModel()
        obj2 = FileStorage()
        obj2.new(obj1)
        self.assertIn(obj1, obj2.all().values())


class TestFileStorageSave(unittest.TestCase):
    """"Unittests for save method"""

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
        FileStorage._FileStorage__objects = {}

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().save(None)

    def test_save_with_base_model(self):
        obj = BaseModel()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "BaseModel." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_user(self):
        obj = User()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "User." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_amenity(self):
        obj = Amenity()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "Amenity." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_city(self):
        obj = City()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "City." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_place(self):
        obj = Place()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "Place." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_review(self):
        obj = Review()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "Review." + obj.id
            self.assertIn(key, file.read())

    def test_save_with_state(self):
        obj = State()
        obj.save()

        with open("file.json", "r", encoding="UTF-8") as file:
            key = "State." + obj.id
            self.assertIn(key, file.read())

    def test_reload_with_base_model(self):
        obj = BaseModel()
        obj.save()
        storage.reload()
        key = "BaseModel." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_amenity(self):
        obj = Amenity()
        obj.save()
        storage.reload()
        key = "Amenity." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_city(self):
        obj = City()
        obj.save()
        storage.reload()
        key = "City." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_place(self):
        obj = Place()
        obj.save()
        storage.reload()
        key = "Place." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_review(self):
        obj = Review()
        obj.save()
        storage.reload()
        key = "Review." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_state(self):
        obj = State()
        obj.save()
        storage.reload()
        key = "State." + obj.id
        self.assertIn(key, storage.all().keys())

    def test_reload_with_user(self):
        obj = User()
        obj.save()
        storage.reload()
        key = "User." + obj.id
        self.assertIn(key, storage.all().keys())


class TestFileStorageReload(unittest.TestCase):
    """Unittests for reload method"""

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().reload(None)

if __name__ == '__main__':
    unittest.main()
