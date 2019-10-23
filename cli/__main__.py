import click
import traceback
from core.services import console_emitter_service, dest_file_emitter_service, severity_parser_service
from core.services import run_file_logic_service, run_folder_logic_service


@click.command()
@click.option('--path', required=True, help='This is the path to the file to parse')
@click.option('--is-directory', is_flag=True, help='This is a flag that indicates if the path passed is a file or directory')
@click.option('--severity', default='ERROR', help='This is the severity of the log you want to get')
@click.option('--console', default=True, is_flag=True)
@click.option('--dest-file', help='This is the path to which the results will be written')
def cli(path, is_directory, severity, console, dest_file):
    try:
        parsers = []
        emitters = []
        parsers.append(severity_parser_service(severity))
        if console:
            emitters.append(console_emitter_service())
        if dest_file:
            emitters.append(dest_file_emitter_service(dest_file))
        if is_directory:
            run_folder_logic_service(path, parsers, emitters)
        else:
            run_file_logic_service(path, parsers, emitters)
    except Exception as e:
        traceback.print_exc()
        raise click.ClickException(e)


if __name__ == '__main__':
    cli()
