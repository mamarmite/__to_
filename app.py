
import random
import os
import sys

# python 3.5 et +
import pathlib



from Command import Command
from Entry import Entry
from Section import Section
from Type import Type

endline = "\r\n"
base_folder = ""

# clear the console's app response.
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# Add the __to_ the paths to get beautiful command line.

## OOP because my mindset, so is build that way. Methods are always functional though.

def help():
    # print out instructions on how to use the app
    print("This is the __To_ * tool. Classify your every day wanders and finds.")
    print( """
        Use the '__to_' command + the kind of notes you want to add : see, do, listen, read, see, try, code, etc.
        - By default the app save the data in a *.md file.
        Use the add method to setup sections within the __to_note types.
        - list the params like (h1, h2, ...).
    """)


## Functional app's methods.

# base function to dispatch save, remove and save command.

def add(command):
    if (type == 'type'):
        add_type(command)

    elif (type == 'section'):
        print ('add section')

    elif (type == 'entry'):
        print ('add entry to ')


def remove(command):
    if (command.type == 'type'):
        remove_type(command)

    elif (command.type == 'section'):
        print ('remove section')

    elif (command.type == 'entry'):
        print ('remove entry to section')


def save(command):
    if (command.type == 'type'):
        save_type(command)

    elif (command.type == 'section'):
        print ('save section')

    elif (command.type == 'entry'):
        print ('save entry to section')


# TYPE
### need fs.
def add_type(command, **kwargs):

    type_folder_path = "{}{}".format(base_folder, command.type)
    pathlib.Path(type_folder_path).mkdir(parents=True, exist_ok=True) 

    current_file = open('{}/{}.md'.format(type_folder_path, command.target), "w+")

    current_file.write('# __To_ : {}{}'.format(command.target, endline))

    # Check if this exists from global list based on files structure (and history as db, logs, etc.).
    # If not, start the creation of the folder structure
    # Create the init .md of that type.


#commit to github the saved elements.
def save_type(command, **kwargs):
    print('save_type {}'.format(command.target))


def remove_type(command, **kwargs):
    print('remove_type {}'.format(command.target))



# Like a user's input getter, for less refactorin when we will get out of cli.
def ask_user(what):
    return input(what).lower()


def command_dispatcher(command):
    print(command)#print raw command to see what we get.

    if (command.master == 'add'):
        add(command)

    elif (command.master == 'remove'):
        remove(command)

    elif (command.master == 'save'):
        save(command)


### main loop that manage the hole process.
def App():
    help()
    types = []
    
    while True:
        target_command = ask_user("What __to_ ? (q to exit): ")
        current_command = Command(target_command)

        if (current_command.master == 'q' or current_command.master == 'exit' or current_command.master == 'quit'):
            quit_app()

        else:
            command_dispatcher(current_command)


def quit_app():
    print("See you next time, alligator.")
    sys.exit()


App()
# @todos
##  Make an URL Class to manage the link, counts, and everything. To confirm.
##      Check for **kwargs and command line inputs. Because it will start as command line app for now.
###         And think a bit if we'll have a GUI someday.