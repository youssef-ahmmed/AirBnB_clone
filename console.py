#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""

import ast
import cmd
import re
from typing import List

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
    class_names: List[str] = ["BaseModel", "User", "Amenity",
                              "City", "Review", "Place", "State"]
    commands: dict = {"all": "do_all", "count": "do_count", "show": "do_show",
                      "destroy": "do_destroy", "update": "do_update"}

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

    def do_count(self, line) -> None:
        """Count existence of a given class"""
        if self._check_class(line) == "exit":
            return

        count: int = 0
        instance_dict = storage.all()

        for key in instance_dict.keys():
            if key.startswith(line):
                count += 1

        print(count)

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
        storage.save()

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

        if self._handle_dict(line) == "exit":
            return

        if self._check_attribute_and_value(line) == "exit":
            return

        split_line = self._split_line(line)
        if split_line[2].startswith("(") or split_line[2].startswith("["):
            return

        key = split_line[0] + "." + split_line[1]
        storage.update(key, split_line[2], split_line[3])
        (storage.all()[key]).save()

    @staticmethod
    def _split_line(line) -> list:
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

    @staticmethod
    def _check_id(line) -> str:
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

    def _handle_dict(self, line) -> str:
        """Handle dictionary representation"""
        dict_repr = self._check_dict_repr_type(line)
        if dict_repr == {}:
            return "not exit"

        forbidden_attributes = ["updated_at", "created_at", "id"]
        obj_key = line.split()[0] + '.' + line.split()[1]
        for key, val in dict_repr.items():
            if key in forbidden_attributes:
                continue
            storage.update(obj_key, key, val)
        (storage.all()[obj_key]).save()

        return "exit"

    @staticmethod
    def _check_dict_repr_type(line) -> dict:
        """Check type of dict and convert it form string"""
        match = re.search(r'\[(.*?)]\s*|({.*?})\s*|(\(.+?\))', line)
        if not match:
            return {}

        dict_str = match.group()
        try:
            dict_repr = ast.literal_eval(dict_str)
            if type(dict_repr) != dict:
                return {}
        except (ValueError, SyntaxError):
            return {}

        return dict_repr

    @staticmethod
    def _check_attribute_and_value(line) -> str:
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

    def default(self, line: str) -> None:
        """Called on an input line when the command prefix is not recognized"""
        class_name = re.search(r"\w+(?=\.)", line)
        class_name = class_name.group() if class_name else None

        func = re.search(r"(?<=\.)\w+(?=\()", line)
        func = func.group() if func else None

        if (self._check_error_for_instance_by_name(func, class_name, line)
                == "exit"):
            return

        func_args = re.search(r"(?<=\().(?P<args>.*?)(?=\))", line)
        func_args_str = ""
        if func_args:
            func_args = func_args.group()
            if self._search_for_dict(class_name, func_args, func) == "exit":
                return

            func_args_str = " ".join(func_args.replace('"', "")
                                     .replace("'", "")
                                     .replace(", ", ",")
                                     .split(","))

        func_args_str = (class_name if not func_args_str
                         else f"{class_name} {func_args_str}")
        getattr(self, self.commands[func])(func_args_str)

    def _check_error_for_instance_by_name(self, func, class_name, line):
        if func in self.commands.keys() and not class_name:
            getattr(self, self.commands[func])("")
            return "exit"

        if func not in self.commands.keys():
            self.stdout.write('*** Unknown syntax: %s\n' % line)
            return "exit"

    def _search_for_dict(self, class_name, func_args, func) -> str:
        match = re.search(r'\[(.*?)]\s*|({.*?})\s*|(\(.+?\))', func_args)
        if match:
            match = match.group()
            func_args = (func_args.split(',')[0]).replace("'", "") \
                .replace('"', "")
            func_args_str = class_name + " " + func_args + " " + match
            getattr(self, self.commands[func])(func_args_str)
            return "exit"

    @staticmethod
    def help_create() -> None:
        """help create function"""
        print("Creates a new instance of a given class\n")

    @staticmethod
    def help_count() -> None:
        """help count function"""
        print("Retrieve the number of instances of a class\n")

    @staticmethod
    def help_show() -> None:
        """help show function"""
        print("Prints the string representation of an"
              "instance based on the class name and id\n")

    @staticmethod
    def help_destroy() -> None:
        """help destroy function"""
        print("Deletes an instance based on the class name and id\n")

    @staticmethod
    def help_all() -> None:
        """help all function"""
        print("Prints all string representation of all instances "
              "based or not on the class name\n")

    @staticmethod
    def help_update() -> None:
        """help update function"""
        print("Updates an instance based on the class name "
              "and id by adding or updating attribute\n")

    @staticmethod
    def help_quit() -> None:
        """help quit function"""
        print("Quit command to exit the program\n")

    @staticmethod
    def help_EOF() -> None:
        """help EOF command"""
        print("EOF command to exit the program\n")

    @staticmethod
    def do_quit(line) -> bool:
        """Quit command to exit the program"""
        return True

    @staticmethod
    def do_EOF(line) -> bool:
        """EOF command to exit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
