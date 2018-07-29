# Manage the files, the sections of these files and entries.
class Type:

    def help():
        # print out instructions on how to use the app
        print("Manage the files contains in one type. * For now design means 1, but i would be cool tho make that parametrable, but it's a 2 : so next version..")

    # title
    # path
    # files * one for now, multiple is a 2.
    # contents

    def __init__(self, title='', path='', files=[], contents=[], **kwargs):
        self.title = title
        self.path = path
        self.files = files
        self.contents = contents
        self.sections = []

        for key, value in kwargs.items():
            setattr(key, value)


    # Need a section instance.
    def add_section(self, section):
        self.sections.append(section)


    # Do __append__ instead ?
    def add_entry(self, section_id, entry):
        self.sections[section].append(entry)

    def create_file(self):
        print("create_file from Type")
        #title name with no spaces and specials char.


    def remove_section(self, section_id):
        # loop through sections and remove by id.
        for key, section in self.sections:
            if (section.id == section_id):
                self.sections.remove(section)


    # Do __append__ instead ?
    def remove_entry(self, section_id, entry):
        # Loop through section and after through entries.
        # loop through sections and remove by id.
        for key, section in self.sections:
            if (section.id == section_id):
                for key, entry in section.entries:
                    section.entries.remove(entry)

