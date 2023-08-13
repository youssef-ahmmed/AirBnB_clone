"""Defines unittests for console module"""

import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestHBNBCommandPrompt(unittest.TestCase):
    """Unittests for prompting cmd"""

    def test_prompt(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(HBNBCommand().prompt, "(hbnb) ")

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue())


class TestHBNBCommandExit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommandHelp(unittest.TestCase):
    """Unittests for help commands"""

    def test_help_with_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            expected_result = ("Documented commands (type help <topic>):\n"
                               "========================================\n"
                               "EOF  all  count  create  destroy  help  quit  show  update")
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            expected_result = "Quit command to exit the program"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            expected_result = "EOF command to exit the program"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            expected_result = "Prints all string representation of all instances " \
                              "based or not on the class name"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            expected_result = "Retrieve the number of instances of a class"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            expected_result = "Creates a new instance of a given class"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            expected_result = "Deletes an instance based on the class name and id"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            expected_result = "Prints the string representation of an" \
                              "instance based on the class name and id"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            expected_result = "Updates an instance based on the class name " \
                              "and id by adding or updating attribute"
            self.assertEqual(expected_result, f.getvalue().strip())


class TestHBNBCommandCreate(unittest.TestCase):
    """Unittests for create command"""

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
        FileStorage._FileStorage__objects = {}

    def test_create_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected_result = "** class name missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".create()")
            expected_result = "*** Unknown syntax: .create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModule")
            expected_result = "** class doesn't exist **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModule.create()")
            expected_result = "*** Unknown syntax: MyModule.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            expected_result = "*** Unknown syntax: BaseModel.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            expected_result = "*** Unknown syntax: Amenity.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            expected_result = "*** Unknown syntax: City.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            expected_result = "*** Unknown syntax: Place.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            expected_result = "*** Unknown syntax: Review.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            expected_result = "*** Unknown syntax: State.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_instance_by_class_name_with_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            expected_result = "*** Unknown syntax: User.create()"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_create_with_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            key = "BaseModel." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            key = "Amenity." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            key = "User." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            key = "City." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            key = "Place." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            key = "Review." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            key = "State." + f.getvalue().strip()
            self.assertIn(key, storage.all().keys())

    def test_create_with_more_than_one_arg(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State City BaseModel")
            key1 = "State." + f.getvalue().strip()
            key2 = "City." + f.getvalue().strip()
            key3 = "BaseModel." + f.getvalue().strip()
            self.assertIn(key1, storage.all().keys())
            self.assertNotIn(key2, storage.all().keys())
            self.assertNotIn(key3, storage.all().keys())


class TestHBNBCommandShow(unittest.TestCase):
    """Unittests for show command"""

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
        FileStorage._FileStorage__objects = {}

    def test_show_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            expected_result = "** class name missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_no_args(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
            expected_result = "** class name missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModule")
            expected_result = "** class doesn't exist **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModule.show()")
            expected_result = "** class doesn't exist **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_base_model_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_base_model_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_amenity_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_amenity_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_city_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_city_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_place_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_place_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_review_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_review_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_state_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_state_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_user_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_user_and_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            expected_result = "** instance id missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_base_model_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_base_model_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_Amenity_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_Amenity_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_city_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_city_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_place_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_place_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_review_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_review_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_state_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_state_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_user_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 12396")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_instance_by_class_name_with_user_and_wrong_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(12396)")
            expected_result = "** no instance found **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_show_with_valid_base_model(self):
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_base_model(self):
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_amenity(self):
        obj = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_amenity(self):
        obj = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_city(self):
        obj = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_city(self):
        obj = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_place(self):
        obj = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_place(self):
        obj = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_review(self):
        obj = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_review(self):
        obj = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_state(self):
        obj = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_state(self):
        obj = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_with_valid_user(self):
        obj = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())

    def test_show_instance_by_class_name_with_valid_user(self):
        obj = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show({})".format(obj.id))
            self.assertEqual(str(obj), f.getvalue().strip())


class TestHBNBCommandCount(unittest.TestCase):
    """Unittests for show command"""

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
        FileStorage._FileStorage__objects = {}

    def test_count_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            expected_result = "** class name missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_count_instance_by_name_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".count()")
            expected_result = "** class name missing **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_count_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyModule")
            expected_result = "** class doesn't exist **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_count_instance_by_name_with_wrong_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModule.count()")
            expected_result = "** class doesn't exist **"
            self.assertEqual(expected_result, f.getvalue().strip())

    def test_count_with_base_model(self):
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_base_model(self):
        obj = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_amenity(self):
        obj = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Amenity")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_amenity(self):
        obj = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_city(self):
        obj = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count City")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_city(self):
        obj = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_place(self):
        obj = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Place")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_place(self):
        obj = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_review(self):
        obj = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count Review")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_review(self):
        obj = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_state(self):
        obj = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_state(self):
        obj = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_with_user(self):
        obj = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertEqual("1", f.getvalue().strip())

    def test_count_instance_by_name_with_user(self):
        obj = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("1", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
