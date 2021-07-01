#!/usr/bin/env python3
"""
Command line interpreter for AirBnB console
Interface to interact with programs
"""
import cmd
from models.engine.file_storage import all_classes
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This the console """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save to JSON file, print id
        """
        if not arg:
            print("** class name missing **")
        elif arg in all_classes:
            myModel = all_classes[arg]()
            storage.new(myModel)
            storage.save()
            print(myModel.id)
        else:
            print("** class doesn't exist **")

    @staticmethod
    def key_validator(arg):
        """ validates key for show method """
        key = None
        change_key = None
        argv = arg.split()
        argc = len(argv)
        if not arg:
            print("** class name missing **")
        elif argv[0] not in all_classes:
            print("** class doesn't exist **")
        elif argc < 2:
            print("** instance id missing **")
        else:
            argv[1] = argv[1].strip('",')
            change_key = '.'.join(argv[0:2])
            if change_key not in storage.all():
                print("** no instance found **")
            else:
                key = change_key
        return key

    def do_show(self, arg):
        """ Print string representation of instance, given id """
        key = HBNBCommand.key_validator(arg)
        if key:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """ Delete instanced based on class name and id """
        key = HBNBCommand.key_validator(arg)
        if key:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        argv = arg.split()
        if not arg:
            for val in storage.all().values():
                print(val)
        elif argv[0] in all_classes:
            for key, value in storage.all().items():
                if key[0: key.index('.')] == argv[0]:
                    print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instanced based on class name and id """
        key = HBNBCommand.key_validator(arg)
        if key:
            argv = list(arg.split())
            argc = len(argv)
            if argc < 3:
                print("** attribute name missing **")
            elif argc < 4:
                print("** value missing **")
            elif storage.all():
                for key in storage.all().keys():
                    update_model = storage.all()[key]
                    strip_argv3 = argv[3].strip('"')
                    setattr(update_model, argv[2], strip_argv3)
                    update_model.save()
                    storage.reload()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ End Of File condition to terminate program
        """
        print()
        return True

    def emptyline(self):
        """ Allows prompt to not be repeated constantly
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
