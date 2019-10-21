import click
from core.services.file import file_severity_to_console


@click.command()
@click.option('--file', required=True, help='This is the path to the file to parse')
@click.option('--level', default='ERROR', help='This is the level of the log you want to get')
@click.option('--console', default=True, is_flag=True)
def cli(file, level, console):
    if console:
        file_severity_to_console(file, level)
    else:
        print("Please select the printing option :)")


if __name__ == '__main__':
    cli()
