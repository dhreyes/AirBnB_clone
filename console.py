#!/usr/bin/python3
"""
Command line interpreter for AirBnB console
Interface to interact with programs
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ This the console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ End Of File condition to terminate program """
        print()
        return True

    def emptyline(self):
        """ Allows prompt to not be repeated constantly """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
