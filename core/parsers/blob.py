def run_parsers_on_blob(lines, parsers, remove_duplicates=False):
    parsed_lines = []
    [parsed_lines.extend(parser(lines)) for parser in parsers]
    if remove_duplicates:
        return list(set(parsed_lines))
    return parsed_lines
