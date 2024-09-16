#!/usr/bin/python3
"""Command line interpreter"""

import cmd, sys



class HBNBCommand(cmd.Cmd):
    intro = "Welcome to my AirBnB console, Type help or ? to list commands \n"
    prompt = '(HBNB)'
    file = None



    def do_EOF(self, line):
        """Exit interpreter"""
        return True

    def postcmd(self, stop, line):
        """Clean up after exiting"""
        return stop

    def do_quit(self, line):
        """Quit the command line intrepreter"""
        print("Cheers !!")

        return True









if __name__ == "__main__":
    HBNBCommand().cmdloop()
