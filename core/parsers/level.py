def _is_line_severe(line, severity):
    return severity in line


# Its this way so we don't use classes, if needed, the implementation can be switched to classes
# and the logic in this function can be replaced with a constructor.
def get_parser_by_severity(severity):
    def inner(lines):
        parsed_lines = []
        for line in lines:
            if _is_line_severe(line, severity):
                parsed_lines.append(line)
        return parsed_lines

    return inner



