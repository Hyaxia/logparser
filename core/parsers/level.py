from core.model.parser import ABCParser


class SeverityParser(ABCParser):
    def __init__(self, severity):
        self.severity = severity

    def _is_line_severe(self, line):
        return self.severity in line

    def parse(self, lines):
        parsed_lines = []
        for line in lines:
            if self._is_line_severe(line):
                parsed_lines.append(line)
        return parsed_lines

