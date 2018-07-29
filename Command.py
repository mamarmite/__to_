class Command:

    def help():
        print("This is a class to manage a full length command from the console or other sources.")
        print("The program will consider the first to be the master command, like add remove or save")
        print("'master' 'type' 'target' 'content' 'flag1' 'flag2' 'flag3'")

    def __init__(self, commands):
        self.raw = commands

        self.commands_name = ['master', 'type', 'target', 'file', 'content', 'flag1', 'flag2', 'flag3']

        # Default set the command's name.
        for keyword in self.commands_name:
            setattr(self, keyword, "")

        self.parse_command(self.raw)


    # Kind of a mapping function.
    def parse_command(self, command):
        self.all = command.split()
        index = 0
        for value in self.all:

            if (index < len(self.commands_name)):
                setattr(self, self.commands_name[index], value)

            else:
                print("* Warning : The command have more params than needed.")
                break
            index += 1

    def __str__(self):
        return "Command object : {} {} {} {} {} {} {}".format(self.master, self.type, self.target, self.file, self.content, self.flag1, self.flag2, self.flag3)
