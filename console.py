#!/usr/bin/python3

"""Command line interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interpreter"""

    prompt = '(hbnb) '
    file = None

    def do_create(self, class_name):
        """Create a new instance of a class"""
        if not class_name:
            print("** class name missing **")
            return
        
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        
        instance = eval(class_name)()  # Create an instance of the class
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, class_name=""):
        """Prints all string representation of all instances or of a specific class"""
        if class_name and class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        
        objects = storage.all()
        if class_name:
            fobjects = [str(obj) for key, obj in objects.items() if key.startswith(class_name)]
        else:
            fobjects = [str(obj) for obj in objects.values()]

        print("[" + ", ".join(fobjects) + "]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else 
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        instance = objects[key]

        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()
        print("Instance updated.")

    def do_EOF(self, line):
        """Exit interpreter"""
        return True

    def do_quit(self, line):
        """Quit the command line interpreter"""
        print("Cheers !!")
        return True

    def emptyline(self):
        """Disable repeating the last command"""
        return None


if __name__ == "__main__":
    """Main loop"""
    HBNBCommand().cmdloop()

