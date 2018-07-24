# Manage the section within a Type file.
class Section:

    def help():
        print("Manage the section within a Type file.")

    # id #this kinda become like a model. Should I implement an auto increment like a thing ?
    # title
    # description
    # entries
    # is_all_toed

    def __init__(self, id=0, title='', description='', entries=[], **kwargs):
        self.title = title
        self.description = path
        self.is_all_toed = false
        self.entries = entries

        for key, value in kwargs.items():
            setattr(key, value)

    # Dry alert (same needs for Entry and Section, need a super ?)
    # Do __append__ instead ?
    #def add_entry(self, section_id, entry):
        # self.sections[section].append(entry)


    # Do __append__ instead ?
    #def remove_entry(self, section_id, entry):
        # self.sections[section].remove(entry)
