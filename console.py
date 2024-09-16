#!/usr/bin/python3
"""Command line interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command line intrepreter"""

    intro = "Welcome to my AirBnB console, Type help or ? to list commands \n"
    prompt = '(hbnb)'
    file = None

    def do_EOF(self, line):
        """Exit interpreter"""

        return True

    def do_quit(self, line):
        """Quit the command line intrepreter"""

        print("Cheers !!")

        return True

    def emptyline(self):
        """Disable repeating the last command"""

        return None


if __name__ == "__main__":
    """"""

    HBNBCommand().cmdloop()
