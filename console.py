#!/usr/bin/python3
"""Console Interpreter"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class command"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_create(self, arg):
        """Creat a new instance of BaseModel"""

        if len(arg) < 1:  # if class name is missing
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:  # class name no exist
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()  # save into file json
            print("{}".format(new.id))

    def do_show(self, arg):
        """Print string rep. of an instance based on class name"""

        args = arg.split()
        data_list = []
        if len(args) < 1:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                data_list.append("[{}] ({}) {}".format(args[0],
                                 args[1], storage.all()[key]))
                print(data_list)

    def do_destroy(self, arg):
        """Delete an instance based on class name"""

        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """Print all string rep. of instance"""

        args = shlex.split(arg)
        data_list = []
        if len(arg) < 1:
            for key, value in storage.all().items():
                c_name, c_id = key.split(".")
                data_list.append("{}".format(value))
            print(data_list)
        else:
            if not args[0] in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    c_name, c_id = key.split(".")
                    if c_name == args[0]:
                        data_list.append("{}".format(value))
                print(data_list)

    def do_update(self, arg):
        """Update an instance based on class name"""

        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all().get(key)
                    setattr(obj, args[2], args[3])
                    storage.save()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
