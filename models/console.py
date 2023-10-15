#!/usr/bin/python3
"""A program that contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
