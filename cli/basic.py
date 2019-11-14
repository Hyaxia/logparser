import argparse
import traceback
import sys
from core.services import console_emitter_service, dest_file_emitter_service, severity_parser_service
from core.services import run_file_logic_service, run_folder_logic_service


def cli():
    parser = argparse.ArgumentParser(description='CLI for parsing logs.')
    parser.add_argument('--path', type=str, dest='path', help='an integer for the accumulator')
    parser.add_argument('--is-directory', action='store_true', dest='is_directory', help='This is a flag that indicates if the path passed is a file or directory')
    parser.add_argument('--no-console', action='store_false', dest='console')
    parser.add_argument('--dest-file', dest='dest_file', type=str, help='This is the path to which the results will be written',)
    parser.add_argument('--severity', dest='severity', type=str, help='This is the severity of the log you want to get')
    parser.set_defaults(dest_file=False, severity='ERROR')

    args = parser.parse_args(sys.argv[1:])
    try:
        parsers = []
        emitters = []
        parsers.append(severity_parser_service(args.severity))
        if args.console:
            emitters.append(console_emitter_service())
        if args.dest_file:
            emitters.append(dest_file_emitter_service(args.dest_file))
        if args.is_directory:
            run_folder_logic_service(args.path, parsers, emitters)
        else:
            run_file_logic_service(args.path, parsers, emitters)
    except Exception as e:
        traceback.print_exc()
        raise


if __name__ == '__main__':
    cli()


