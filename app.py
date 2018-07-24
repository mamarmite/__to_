from Type import Type
from Section import Section
from Entry import Entry


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

### Get the right type obj and add this entry.
def save_entry(type, entry, **kwargs):
    target_type = type
    # Get the type OBJ, return the rigth obj from the factory thing to
    # check if that entry is already there or try to find if there is multiple entry that's alike.
    # Add the entry at that line or
    # If instruction is set, 


### need fs.
def add_type(name, **kwargs):
    label = name
    # Check if this exists from global list based on files structure (and history as db, logs, etc.).
    # If not, start the creation of the folder structure
    # Create the init .md of that type.
    # 


### main loop that manage the hole process.
def App():
    help()
    types = []
    

# @todos
##  Make an URL Class to manage the link, counts, and everything. To confirm.
##      Check for **kwargs and command line inputs. Because it will start as command line app for now.
###         And think a bit if we'll have a GUI someday.