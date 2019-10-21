def run_parsers_on_blob(lines, parsers, no_duplicates=False):
    parser_results = []
    [parser_results.append(parser(lines)) for parser in parsers]
    parsed_lines = []
    [parsed_lines.extend(result) for result in parser_results]
    if no_duplicates:
        return list(set(parsed_lines))
    return parsed_lines
