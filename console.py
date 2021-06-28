#!/usr/bin/python3
"""
Command line interpreter for AirBnB console
Interface to interact with programs
"""
import cmd
from models import all_classes
from models import storage

class HBNBCommand(cmd.Cmd):
    """ This the console """
    prompt = "(hbnb) "
    intro = "Welcome to our HBnB console! Type ? or help for commands"

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save to JSON file, print id
        """
        if not arg:
            print("** class name missing **")
        elif arg in all_classes:
            new_instance = all_classes[arg]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    @staticmethod
    def key_validator(arg):
        """ validates key for show method """
        pass

    def do_show(self, arg):
        """ Print string representation of instance, given id """
        pass

    def do_destroy(self, arg):
        """ Delete instanced based on class name and id """
        pass

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        pass

    def do_update(self, arg):
        """ Updates an instanced based on class name and id """
        pass

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
