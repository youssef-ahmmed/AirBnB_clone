#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""

import cmd

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines command line interpreter"""

    prompt: str = "(hbnb) "
    class_names = ["BaseModel", "User", "Amenity",
                   "City", "Review", "Place", "State"]

    def emptyline(self):
        """Add new line when pressing enter"""
        print("", end="")

    def do_create(self, line):
        """Creates a new instance of a given class"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        obj = eval(class_name)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an
            instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        try:
            class_id = line.split()[1]
        except IndexError:
            print("** instance id missing **")
            return

        key = class_name + "." + class_id
        instance_dict = storage.all()
        if key not in instance_dict.keys():
            print("** no instance found **")
            return
        print(instance_dict[key])

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name"""
        if line and line.split()[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        instance_dict = storage.all()
        list_of_str = []
        for key, val in instance_dict.items():
            if not line or key.startswith(line.split()[0]):
                list_of_str.append(str(val))

        print(list_of_str)

    def help_create(self):
        print("Creates a new instance of a given class\n")

    def help_show(self):
        print("Prints the string representation of an"
              "instance based on the class name and id\n")

    def help_all(self):
        print("Prints all string representation of all instances "
              "based or not on the class name\n")

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
