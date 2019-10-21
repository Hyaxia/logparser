class Blob(object):
    def __init__(self, name, lines, info=None):
        self.name = name
        self.lines = lines
        self.info = info

    def __str__(self):
        return "name: {}, additional info: {}, \n {}".format(self.name, self.info, self.lines)



