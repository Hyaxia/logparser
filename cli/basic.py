import argparse
import traceback
import sys
from core.services import console_emitter_service, dest_file_emitter_service, severity_parser_service
from core.services import file_reader_service, folder_reader_service, main_logic


def cli():
    parser = argparse.ArgumentParser(description='CLI for parsing logs.')
    parser.add_argument('--path', type=str, dest='path', help='path to the file file we want to parse')
    parser.add_argument('--directory-path', type=str, dest='directory_path', help='path to the folder we want to parse')
    parser.add_argument('--no-console', action='store_false', dest='console')
    parser.add_argument('--dest-file', dest='dest_file', type=str, help='This is the path to which the results will be written',)
    parser.add_argument('--severity', dest='severity', type=str, help='This is the severity of the log you want to get')
    parser.set_defaults(dest_file=False, severity='ERROR')

    args = parser.parse_args(sys.argv[1:])
    try:
        readers = []
        parsers = []
        emitters = []
        parsers.append(severity_parser_service(args.severity))
        if args.console:
            emitters.append(console_emitter_service())
        if args.dest_file:
            emitters.append(dest_file_emitter_service(args.dest_file))
        if args.path:
            readers.append(file_reader_service(args.path))
        if args.directory_path:
            readers.append(folder_reader_service(args.directory_path))
        if len(readers) == 0:
            raise Exception('no reader functions were chosen')
        main_logic(readers, parsers, emitters)

    except Exception as e:
        traceback.print_exc()
        raise


if __name__ == '__main__':
    cli()


