from core.model.blob import Blob


def raw_input_reader(raw_input):
    """
    This reader function will handle any raw input that is given to it
    by splitting the input into lines and removing any redundant spaces.
    :param raw_input: raw string
    :return: list of strings, each index represents new line
    """
    lines = raw_input.split('\n')
    name = "Console Input"
    return Blob(name, lines)


