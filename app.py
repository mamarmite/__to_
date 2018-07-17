

# Add the __to_ the paths to get beautiful command line.

# OOP or functionnal ? Always both, but need the thinking of it before coding.


def help():
    # print out instructions on how to use the app
    print("This is the __To_ * tool. Classify your every day wanders and finds.")
    print( """
        Use the '__to_' command + the kind of notes you want to add : see, do, listen, read, see, try, code, etc.
        - By default the app save the data in a *.md file.
        Use the add method to setup sections within the __to_note types.
        - list the params like (h1, h2, ...).
    """)

## OOP because my mindset, so is build that way. Methods are always functional though.


# class: Type
    # manage the files contains in one type. * For now design means 1, but i would be cool tho make that parametrable, but it's a 2 : so next version.
    # Attributes
        # title
        # path
        # files * one for now, multiple is a 2.
        # contents
        # Styles * this maybe needs to be directly in sections or entry?
            # type default # Markdown
            # section_title
            # list_style
    # methods
        # add_section @param Section Obj.
        # add_entry @param Entry Obj.
        # remove_entry @param Entry id. * hard to add id in txt file. maybe line index within the section?
        # remove_section @param Section id. * hard to add id in txt file. maybe line index within the section?


# class: Section
    # Manage the section within a Type file.
    # Attributes
        # title
        # description
        # entries
        # is_all_toed


# class: Entry
    # Manage the entry, can start with the String object, anyhow.
    # Attributes
        # title
        # description
        # link
        # is_toed
        # visited count * Can do stats there.


# Get the right type obj and add this entry.
def save_entry(type, entry, instructions)
    # Get the type OBJ, return the rigth obj from the factory thing to
    # check if that entry is already there or try to find if there is multiple entry that's alike.
    # Add the entry at that line or
    # If instruction is set, 


# 
def add_type(name)
    # Check if this exists from global list based on files structure (and history as db, logs, etc.).
    # If not, start the creation of the folder structure
    # Create the init .md of that type.
    # 


# main loop that manage the hole process.
def App():
    help()
    types = []
    
