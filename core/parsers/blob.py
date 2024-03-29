def run_parsers_on_lines(lines, parsers):
    parser_results = []
    [parser_results.append(parser.parse(lines)) for parser in parsers]
    parsed_lines = []
    [parsed_lines.extend(result) for result in parser_results]
    return parsed_lines
