# Manage the entry, can start with the String object, anyhow.
class Entry:

    def help():
        print("Manage the entry, can start with the String object, anyhow.")

    # title
    # description
    # link
    # is_toed
    # visited count * Can do stats there.

    def __init__(self, title='', description='', link='', is_toed=False, visited=False, **kwargs):
        self.title = title
        self.description = path
        self.is_toed = is_toed
        self.visited = visited

        for key, value in kwargs.items():
            setattr(key, value)
            
