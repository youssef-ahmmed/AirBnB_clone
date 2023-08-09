#!/usr/bin/python3
"""Defines the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines command line interpreter"""

    prompt: str = "(hbnb) "

    def emptyline(self):
        """Add new line when pressing enter"""
        print("", end="")

    def do_quit(self, _line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, _line):
        """EOF command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
