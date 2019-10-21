from enum import Enum


class LogLineSeverity(Enum):
    """
    This class holds the values by which we can check if a line is a certain level of log.
    If the line contains a value that is listen in the parameter of this class,
    for example, an `Error:` value, then it is an ERROR level log line.
    """
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'

    @staticmethod
    def validate_severity(input_level):
        for level in LogLineSeverity:
            if input_level == level.name:
                return input_level
        raise Exception('No such severity exists')

