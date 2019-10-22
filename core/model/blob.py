class Blob(object):
    def __init__(self, name, lines, info=None):
        self.name = name
        self.lines = lines
        self.info = info

    def __str__(self):
        additional_info_as_string = ''
        for key, value in self.info.items():
            additional_info_as_string += "{}: {}".format(key, value)
        lines_as_string = ''.join(self.lines)
        return "name: {},\nadditional info: {},\n\n{} \n -----------------------------------------------------\n"\
            .format(self.name, additional_info_as_string, lines_as_string)



