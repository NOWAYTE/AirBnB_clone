#!/usr/bin/python3

"""Command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interpreter"""

    prompt = '(hbnb)'
    file = None

    def do_create(self, name):
        """Create a new instance of BaseModel class"""
        if not name:
            print("** class name missing **")
            return

        if name != "BaseModel":
            print(f"** class {name} doesn't exist **")
            return

        instance = BaseModel()
        instance.save()
        print("{}".format(instance.id))

    def do_show(self, arg):
        """Prints string representation of instance"""
        args = arg.split()

        if len(args) == 0:
            print("** class name is missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        class_id = args[1]

        key = f"{class_name}.{class_id}"
        objects = storage.all()

        if key in objects:
            print("{}".format(objects[key]))
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and ID"""
        args = arg.split()

        if len(args) == 0:
            print("** class name is missing **")
            return

        if args[0] != "BaseModel":
            print(f"** class name doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        class_id = args[1]

        key = f"{class_name}.{class_id}"
        objects = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
            print(f"Instance {class_name}.{class_id} deleted")
        else:
            print("** no instance found **")

    def do_all(self, class_name=""):
        """Prints all string representations of all instances or by class"""
        objects = storage.all()

        if class_name and class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        fobjects = [str(obj) for key, obj in objects.items()
                    if not class_name or key.startswith(class_name)]

        for obj in fobjects:
            print(obj)

    def do_update(self, arg):
        """Updates an instance based on class name and ID"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')

        if attribute in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return

        instance = objects[key]

        try:
            attribute_type = type(getattr(instance, attribute))
            if attribute_type == int:
                attribute_value = int(attribute_value)
            elif attribute_type == float:
                attribute_value = float(attribute_value)
            else:
                attribute_value = str(attribute_value)
        except AttributeError:
            print(f"** attribute '{attribute}' doesn't exist **")
            return

        setattr(instance, attribute, attribute_value)
        instance.save()
        print(f"Instance {key} updated successfully")

    def do_EOF(self, line):
        """Exit the interpreter"""
        return True

    def do_quit(self, line):
        """Quit the command line interpreter"""
        print("Cheers!!")
        return True

    def emptyline(self):
        """Disable repeating the last command"""
        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
