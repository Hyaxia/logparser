import click
import traceback
from core.services import console_emitter_service, dest_file_emitter_service, severity_parser_service
from core.services import run_file_logic_service


@click.command()
@click.option('--file', required=True, help='This is the path to the file to parse')
@click.option('--severity', default='ERROR', help='This is the severity of the log you want to get')
@click.option('--console', default=True, is_flag=True)
@click.option('--no-duplicates', default=False, is_flag=True)
@click.option('--dest-file', help='This is the path to which the results will be written')
def cli(file, severity, console, no_duplicates, dest_file):
    try:
        parsers = []
        emitters = []
        parsers.append(severity_parser_service(severity))
        if console:
            emitters.append(console_emitter_service())
        if dest_file:
            emitters.append(dest_file_emitter_service(dest_file))
        run_file_logic_service(file, parsers, emitters, no_duplicates)
    except Exception as e:
        traceback.print_exc()
        raise click.ClickException(e)


if __name__ == '__main__':
    cli()
