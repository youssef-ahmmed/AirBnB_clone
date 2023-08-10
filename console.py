#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""

import cmd
import re

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

    def emptyline(self) -> None:
        """Add new line when pressing enter"""
        print("", end="")

    def do_create(self, line) -> None:
        """Creates a new instance of a given class"""
        if self._check_class(line) == "exit":
            return

        obj = eval(line.split()[0])()
        obj.save()
        print(obj.id)

    def do_show(self, line) -> None:
        """Prints the string representation of an
            instance based on the class name and id"""
        if self._check_class(line) == "exit":
            return

        if self._check_id(line) == "exit":
            return

        key = line.split()[0] + "." + line.split()[1]
        instance_dict = storage.all()
        print(instance_dict[key])

    def do_destroy(self, line) -> None:
        """Deletes an instance based on the class name and id"""

        if self._check_class(line) == "exit":
            return

        if self._check_id(line) == "exit":
            return

        key = line.split()[0] + "." + line.split()[1]
        storage.delete(key)
        (storage.all()[key]).save()

    def do_all(self, line) -> None:
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

    def do_update(self, line) -> None:
        """Updates an instance based on the class name
        and id by adding or updating attribute"""

        if self._check_class(line) == "exit":
            return

        if self._check_id(line) == "exit":
            return

        if self._check_attribute_and_value(line) == "exit":
            return

        split_line = self._split_line(line)
        key = split_line[0] + "." + split_line[1]
        storage.update(key, split_line[2], split_line[3])
        (storage.all()[key]).save()

    def _split_line(self, line) -> list:
        """Split the line and Return a list of arguments"""
        split_line = re.findall(r'[^"\s]+|".*?"', line)
        split_line = [
            part.strip('"') if part.startswith('"') else part
            for part in split_line
        ]
        return split_line

    def _check_class(self, line) -> str:
        """"Checks if the class is existed"""
        if not line:
            print("** class name missing **")
            return "exit"

        if line.split()[0] not in self.class_names:
            print("** class doesn't exist **")
            return "exit"

    def _check_id(self, line) -> str:
        """Checks if the id is existed"""
        try:
            class_id = line.split()[1]
        except IndexError:
            print("** instance id missing **")
            return "exit"

        key = line.split()[0] + "." + class_id
        instance_dict = storage.all()
        if key not in instance_dict.keys():
            print("** no instance found **")
            return "exit"

    def _check_attribute_and_value(self, line) -> str:
        """Checks attribute snd value are existed"""
        try:
            line.split()[2]
        except IndexError:
            print("** attribute name missing **")
            return "exit"

        try:
            line.split()[3]
        except IndexError:
            print("** value missing **")
            return "exit"

    def help_create(self) -> None:
        """help create function"""
        print("Creates a new instance of a given class\n")

    def help_show(self) -> None:
        """help show function"""
        print("Prints the string representation of an"
              "instance based on the class name and id\n")

    def help_destroy(self) -> None:
        """help destroy function"""
        print("Deletes an instance based on the class name and id\n")

    def help_all(self) -> None:
        """help all function"""
        print("Prints all string representation of all instances "
              "based or not on the class name\n")

    def help_update(self) -> None:
        """help update function"""
        print("Updates an instance based on the class name "
              "and id by adding or updating attribute\n")

    def do_quit(self, line) -> bool:
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line) -> bool:
        """EOF command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
